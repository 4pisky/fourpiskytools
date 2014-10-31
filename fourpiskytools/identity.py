"""Define the structure of the 'identity' dict."""

class id_keys:
    """Define the dictionary keys as variables

    This gives us two advantages:
     * we get autocompletion in ipython, etc.
     * mistyped key names are caught early (syntax errors) rather than at runtime
       (key-not-in-dict errors)
    """
    address='address'
    stream='stream'
    shortName='shortName'
    contactName='contactName'
    contactEmail='contactEmail'

#Example ID dictionary instance:
example_identity = {
    id_keys.address : 'voevent.organization.tld',
    id_keys.stream : 'ProjectFooAlerts',
    id_keys.shortName : 'ProjectFoo',
    id_keys.contactName : "Jo Bloggs",
    id_keys.contactEmail : "jb@observatory.org",
    }