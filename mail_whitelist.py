from openerp.osv import fields, osv, orm

class mail_whitelist(osv.Model):
    _name = 'mail.whitelist'

    _columns = {
        'model_id': fields.many2one('ir.model', string="Model", required=True),
        'create_log': fields.boolean(string="Create Logging"),
        'create_subscribe': fields.boolean(string="Create Subscriptions"),
        'create_track': fields.boolean(string="Create Tracking"),
    }

    _defaults = {
        'create_log': True,
        'create_subscribe': True,
        'create_track': True,
    }

    _sql_constraints = [('model_id_uniq', 'unique(model_id)', 'You just need to whitelist a model once.')]

class mail_threadwl(osv.Model):
    _inherit = 'mail.thread'
    _name = _inherit

    def is_whitelisted(self, cr, uid, model_name, context=None):
        mail_whitelist = self.pool.get('mail.whitelist')
        res_model = self.pool.get('ir.model').search(cr, uid, [('model', '=', model_name)])
        if res_model:
            res_id = res_model[0]
            res = mail_whitelist.search(cr, uid, [('model_id', '=', res_id)])
            if res:
                obj = mail_whitelist.browse(cr, uid, res[0])
                context = context and dict(context) or {}
                context['mail_create_nolog'] = not obj.create_log
                context['mail_create_nosubscribe'] = not obj.create_subscribe
                context['mail_notrack'] = not obj.create_track
        return context

    def create(self, cr, uid, values, context=None):
        ctx = self.is_whitelisted(cr, uid, self._name, context)
        return super(mail_threadwl, self).create(cr, uid, values, context=ctx)

    def write(self, cr, uid, ids, values, context=None):
        ctx = self.is_whitelisted(cr, uid, self._name, context)
        return super(mail_threadwl, self).write(cr, uid, ids, values, context=ctx)
