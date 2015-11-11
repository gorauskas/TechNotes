<!-- title: Convert a PKCS #12 file into certificate and key files -->

In cryptography, _PKCS #12_ is one of the family of standards called Public-Key
Cryptography Standards published by RSA Laboratories. It defines an archive file
format for storing many cryptography objects as a single file. It is commonly
used to bundle a private key with its X.509 certificate or to bundle all the
members of a chain of trust. A _PKCS #12_ file may be encrypted and signed. The
internal storage containers, called _SafeBags_, may also be encrypted and
signed. A few _SafeBags_ are predefined to store certificates, private keys and
certificate revocation lists. The filename extension for _PKCS #12_ files is
`.p12` or `.pfx`. These files can be created, parsed and read out with the
OpenSSL `pkcs12` command.

I'm going to show you the commands used to convert a `.pfx` file into its
certificate and key components. This information can come in handy when you need
to import your certificates to devices like routers, load-balancers, handhelds,
or for use with webservers like apache or nginx, where you'll need to import the
certificates and key files in plain-text, unencrypted format. Follow these
steps:

1. Install `openssl`
2. Extract the private key:

        openssl pkcs12 -in filename.pfx -nocerts -out encryptedkey.key

3. Enter the `.pfx` file password when prompted
4. Enter a new password for the encrypted key when prompted
5. Extract the client certificate:

        openssl pkcs12 -in filename.pfx -nokeys -clcerts -out certificate.crt

6. Extract the Certificate Authority certificates:

        openssl

7. Sometimes you will need an unencrypted key file:

        openssl rsa -in encryptedkey.key -out decryptedkey.key

8. Enter the key password you created in step 4 above
9. Sometimes the private key needs to be in a PEM format:

        openssl rsa -in encryptedkey.key -outform PEM -out encryptedkey.pem

Always remember to keep your decrypted key in a safe place. Those are the
literal _keys to the kingdom_.
