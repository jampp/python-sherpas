from sharedbuffers import mapped_struct

class PyCon(object):
    __slot_types__ = {
        'num_talks' : int,
        'attendees' : int,
        'Is' : str,
        'talks' : list,
    }
    __slots__ = __slot_types__.keys()
    __schema__ = mapped_struct.Schema.from_typed_slots(__slot_types__)

class PyConArray(mapped_struct.MappedArrayProxyBase):
    schema = PyCon.__schema__

