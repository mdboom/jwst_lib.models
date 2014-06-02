from __future__ import absolute_import, unicode_literals, division, print_function

from . import model_base
from . import wcs


__all__ = ['FringeModel']


class FringeModel(model_base.DataModel, wcs.HasFitsWcs):
    """
    A data model for 2D fringe correction images.
    """
    schema_url = "fringe.schema.json"

    def __init__(self, init=None, data=None, dq=None, err=None, **kwargs):
        super(FringeModel, self).__init__(init=init, **kwargs)

        if data is not None:
            self.data = data

        if dq is not None:
            self.dq = dq

        if err is not None:
            self.err = err
