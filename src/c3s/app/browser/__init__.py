from cone.tile import registerTile
from cone.app.browser.layout import ProtectedContentTile
from c3s.app.model import (
    C3SApp,
    Band,
    Track,
)

from pyramid.view import static
static_view = static('static')

registerTile('content',
             'cone.app:browser/templates/listing.pt',
             interface=C3SApp,
             class_=ProtectedContentTile,
             permission='login',
             strict=False)


registerTile('content',
             'cone.app:browser/templates/listing.pt',
             interface=Band,
             class_=ProtectedContentTile,
             permission='login',
             strict=False)


registerTile('content',
             'c3s.app:browser/templates/track.pt',
             interface=Track,
             class_=ProtectedContentTile,
             permission='login',
             strict=False)
