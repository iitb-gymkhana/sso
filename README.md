OAuth2 Provider for Remote User
===========================
This application usage the standard OAuth2.0 flow described in [RFC 6749](https://tools.ietf.org/html/rfc6749)

Detailed documentation is present at: https://gymkhana.iitb.ac.in/sso/doc/

Special Feature
---------------
- Selective Permissions option for users (like facebook)
- Atomic Permissions for fields

URLs:
-----
**All URLs are from base of application URL. (i.e. assuming application is installed at '/')**  
* Application Registration `/oauth/applications/`
* Authorization `/oauth/authorize/`
* Get Access Token `/oauth/token/`
* Revoke Token `/oauth/revoke_token/`

Scopes:
-------
* **basic**: *Know who you are on SSO*
* **profile**: *Your first name and last name*
* **picture**: *Profile Picture*
* **ldap**: *Your ldap username and email*
* **phone**: *Your contact number including additional numbers*
* **insti_address**: *Your address inside institute*
* **program**: *Your roll number, department, course, joining year and graduation year*
* **secondary_emails**: *Your alternate emails*
* **send_mail**: *Send you mail on behalf of application*

User Resources:
---------------
* **/user/api/user/**: Get basic information corresponding to **basic** scope
* **/user/api/user/?fields=field1,field2**: Get additional information corresponding to field1 and field2. See available fields below

Fields:
-------
**Field Name**: *Required Scopes*
* **first_name**: *profile*
* **last_name**: *profile*
* **profile_picture**: *profile picture*
* **username**: *ldap*
* **email**: *ldap*
* **mobile**: *phone*
* **roll_number**: *program*
* **contacts**: *phone*
* **insti_address**: *insti_address*
* **program**: *program*
* **secondary_emails**: *secondary_emails*

