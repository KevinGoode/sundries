# (C) Copyright 2020 KG
import os
import base64
import ldap
import imghdr


PHOTO_PATH = "/tmp/"


class LdapRequestor(object):


    def save_photos(self, log, url, username, password, scope,
                    query='(objectClass=person)',
                    names={}):
        """
        Serializes users photos to file
        Scope can be domain
        eg scope="DC=companydomain,DC=net"
        or user dn
        eg scope="CN=Fred Bloggs,CN=Users,DC=companydomain,DC=net"
        Default 'query' searches for any user.
        Single user is ;
        "(&(objectClass=user)(SamAccountName=f.bloggs))"
        names is a dictionary of {SamAccountName:filename}
        If name is not found in dict then file is saved using
        filename as  SamAcountName
        """
        results = []
        try:
            # Following option necessary for ldaps (secure) api
            ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT,
                            ldap.OPT_X_TLS_NEVER)
            connect = ldap.initialize(url)
            connect.set_option(ldap.OPT_REFERRALS, 0)
            connect.simple_bind_s(username, password)
            users = connect.search_s(scope,
                                     ldap.SCOPE_SUBTREE,
                                     query,
                                     ['jpegPhoto', 'thumbnailPhoto',
                                      'displayName',
                                      'SamAccountName'])
            for user in users:
                # User is a tuple with 2 items, dn string and dict of
                # requested attributes
                if len(user) == 2:
                    log.info("DN is '**%s**'", user[0])
                    usr = user[1]
                    if 'sAMAccountName' in usr:
                        saved = False
                        image = None
                        # All attributes are lists. Always take first element
                        name = usr['sAMAccountName'][0].decode("utf-8")
                        # Jpeg photo takes precedence over thumbnail
                        if 'jpegPhoto' in usr:
                            image = usr['jpegPhoto'][0]
                        elif 'thumbnailPhoto' in usr:
                            image = usr['thumbnailPhoto'][0]
                        if name and image:
                            filename = name
                            if name in names:
                                filename = names[name]
                            saved = self._bytes_to_file(log, filename, image)
                            if saved is True:
                                log.info("Saved user '%s' photo to file '%s'!",
                                         name, filename)
                        else:
                            log.info("User %s has no photo", name)
                    else:
                        log.error("*Got user without sam acount name*")
                else:
                    log.error("Error reading user attributes")

        except Exception:
            log.exception("Error querying ldap while getting photos")
        return results

    def _bytes_to_file(self, log, filename, byte_stream):
        saved = False
        try:
            extension = imghdr.what("", byte_stream)
            filename = filename.replace(" ", "")
            path = PHOTO_PATH + filename + "." + extension
            with open(path, mode='wb') as file:
                file.write(byte_stream)
            saved = True
        except Exception:
            log.exception("Problem saving picture for user '%s'", filename)
        return saved

