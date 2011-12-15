import cone.app
from c3s.app.model import C3SApp

cone.app.register_plugin('c3sapp', C3SApp)
cone.app.cfg.css.protected.append('c3sapp-static/styles.css')
