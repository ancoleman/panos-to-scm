# /project/scm/obj.py
'''
Most of this came from PANAPI and has been modified - https://github.com/PaloAltoNetworks/panapi/
'''

'''
ISC License

Copyright (c) 2022, Palo Alto Networks Inc.

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
'''

from scm import PanApiHandler

class PanApiHandler:
    """Base class for Pan objects."""
    _endpoint = None  # Default endpoint

    @classmethod
    def get_endpoint(cls):
        """Return the endpoint for the object."""
        if cls._endpoint is None:
            raise NotImplementedError("Endpoint not defined for this object type")
        return cls._endpoint

class SecurityRule(PanApiHandler):
    _endpoint = "/sse/config/v1/security-rules?"

    def __init__(self, api_handler):
        self.api_handler = api_handler

    def list_security_rules(self, folder_scope, limit, position):
        return self.api_handler.list_object(self._endpoint, folder_scope, limit, position)
    
    def move_rule(self, rule_id, folder, destination, destination_rule=None, position="pre"):
        """Move a security rule to a specified position."""
        return self.api_handler.move_security_rule(rule_id, folder, destination, destination_rule, position)

class Address(PanApiHandler):
    "An address object"
    _endpoint = "/sse/config/v1/addresses?"

    def __init__(self, api_handler):
        self.api_handler = api_handler

    def list_address(self, folder_scope, limit='', position=''):
        return self.api_handler.list_object(self._endpoint, folder_scope, limit, position)

class AddressGroup(PanApiHandler):
    "An address group"
    _endpoint = "/sse/config/v1/address-groups?"
    
    def __init__(self, api_handler):
        self.api_handler = api_handler

    def list_address_group(self, folder_scope, limit='', position=''):
        return self.api_handler.list_object(self._endpoint, folder_scope, limit, position)

class Service(PanApiHandler):
    "An application group"
    _endpoint = "/sse/config/v1/services?"
    
    def __init__(self, api_handler):
        self.api_handler = api_handler

    def list_service(self, folder_scope, limit='', position=''):
        return self.api_handler.list_object(self._endpoint, folder_scope, limit, position)
    
class ServiceGroup(PanApiHandler):
    "A service group"
    _endpoint = "/sse/config/v1/service-groups?"
    
    def __init__(self, api_handler):
        self.api_handler = api_handler

    def list_service_group(self, folder_scope, limit='', position=''):
        return self.api_handler.list_object(self._endpoint, folder_scope, limit, position)

class Application(PanApiHandler):
    "An application object"
    _endpoint = "/sse/config/v1/applications?"

class ApplicationFilter(PanApiHandler):
    "An application filter"
    _endpoint = "/sse/config/v1/application-filters?"

    def __init__(self, api_handler):
        self.api_handler = api_handler

    def list_app_filter(self, folder_scope, limit='', position=''):
        return self.api_handler.list_object(self._endpoint, folder_scope, limit, position)

class ApplicationGroup(PanApiHandler):
    "An application group"
    _endpoint = "/sse/config/v1/application-groups?"

    def __init__(self, api_handler):
        self.api_handler = api_handler

    def list_app_group(self, folder_scope, limit='', position=''):
        return self.api_handler.list_object(self._endpoint, folder_scope, limit, position)

class ApplicationOverrideRule(PanApiHandler):
    "An application override rule"
    _endpoint = "/sse/config/v1/app-override-rules?"

class AutoTagAction(PanApiHandler):
    "An auto-tag action"
    _endpoint = "/sse/config/v1/auto-tag-actions?"

class CertificateProfile(PanApiHandler):
    "A certificate profile"
    _endpoint = "/sse/config/v1/certificate-profiles?"

class DynamicUserGroup(PanApiHandler):
    "A dynamic user group"
    _endpoint = "/sse/config/v1/dynamic-user-groups?"

class ExternalDynamicList(PanApiHandler):
    "An external dynamic list"
    _endpoint = "/sse/config/v1/external-dynamic-lists?"

    def __init__(self, api_handler):
        self.api_handler = api_handler

    def list_edl(self, folder_scope, limit='', position=''):
        return self.api_handler.list_object(self._endpoint, folder_scope, limit, position)

class HipObject(PanApiHandler):
    "A HIP object"
    _endpoint = "/sse/config/v1/hip-objects?"

class HipProfile(PanApiHandler):
    "A HIP profile"
    _endpoint = "/sse/config/v1/hip-profiles?"

class Region(PanApiHandler):
    "A region"
    _endpoint = "/sse/config/v1/regions?"

class Schedule(PanApiHandler):
    "A schedule"
    _endpoint = "/sse/config/v1/schedules?"

class Tag(PanApiHandler):
    "A tag object"
    _endpoint = "/sse/config/v1/tags?"

    def __init__(self, api_handler):
        self.api_handler = api_handler

    def list_tag(self, folder_scope, limit='', position=''):
        return self.api_handler.list_object(self._endpoint, folder_scope, limit, position)

class URLCategory(PanApiHandler):
    "A custom URL category"
    _endpoint = "/sse/config/v1/url-categories?"

    def __init__(self, api_handler):
        self.api_handler = api_handler

    def list_urlcategory(self, folder_scope, limit='', position=''):
        return self.api_handler.list_object(self._endpoint, folder_scope, limit, position)

class URLFilteringCategory(PanApiHandler):
    "A predefined URL category"
    _endpoint = "/sse/config/v1/url-filtering-categories?"

class AntiSpywareProfile(PanApiHandler):
    "An anti-spyware profile"
    _endpoint = "/sse/config/v1/anti-spyware-profiles?"

    def __init__(self, api_handler):
        self.api_handler = api_handler

    def list_spywareprofile(self, folder_scope, limit='', position=''):
        return self.api_handler.list_object(self._endpoint, folder_scope, limit, position)

class AntiSpywareSignature(PanApiHandler):
    "An anti-spyware signature"
    _endpoint = "/sse/config/v1/anti-spyware-signature"

class DNSSecurityProfile(PanApiHandler):
    "A DNS security profile"
    _endpoint = "/sse/config/v1/dns-security-profiles?"

class DecryptionExclusion(PanApiHandler):
    "A decryption exclusion"
    _endpoint = "/sse/config/v1/decryption-exclusions?"

class DecryptionProfile(PanApiHandler):
    "A decryption profile"
    _endpoint = "/sse/config/v1/decryption-profiles?"

class DecryptionRule(PanApiHandler):
    "A decryption rule"
    _endpoint = "/sse/config/v1/decryption-rules?"

class FileBlockingProfile(PanApiHandler):
    "A file blocking profile"
    _endpoint = "/sse/config/v1/file-blocking-profiles?"

class HTTPHeaderProfile(PanApiHandler):
    "An HTTP header profile"
    _endpoint = "/sse/config/v1/http-header-profiles?"

class ProfileGroup(PanApiHandler):
    "A profile group"
    _endpoint = "/sse/config/v1/profile-groups?"

    def __init__(self, api_handler):
        self.api_handler = api_handler

    def list_profilegroup(self, folder_scope, limit='', position=''):
        return self.api_handler.list_object(self._endpoint, folder_scope, limit, position)

class URLAccessProfile(PanApiHandler):
    "A URL access profile"
    _endpoint = "/sse/config/v1/url-access-profiles?"

    def __init__(self, api_handler):
        self.api_handler = api_handler

    def list_urlprofile(self, folder_scope, limit='', position=''):
        return self.api_handler.list_object(self._endpoint, folder_scope, limit, position)
    
class VulnerabilityProtectionProfile(PanApiHandler):
    "A vulnerability protection profile"
    _endpoint = "/sse/config/v1/vulnerability-protection-profiles?"

    def __init__(self, api_handler):
        self.api_handler = api_handler

    def list_vulnprofile(self, folder_scope, limit='', position=''):
        return self.api_handler.list_object(self._endpoint, folder_scope, limit, position)

class VulnerabilityProtectionSignature(PanApiHandler):
    "A vulnerability protection signature"
    _endpoint = "/sse/config/v1/vulnerability-protection-signatures?"

class WildFireAntivirusProfile(PanApiHandler):
    "A WildFire antivirus profile"
    _endpoint = "/sse/config/v1/wildfire-anti-virus-profiles?"

    def __init__(self, api_handler):
        self.api_handler = api_handler

    def list_virusprofile(self, folder_scope, limit='', position=''):
        return self.api_handler.list_object(self._endpoint, folder_scope, limit, position)
