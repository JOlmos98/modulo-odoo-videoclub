# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

# class my_module(models.Model):
#     _name = 'my_module.my_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class genero(models.Model):
    _name = 'videoclub.genero'
    _description = 'videoclub.genero'

    nombre = fields.Char(string="Genero", required=True)

class director(models.Model):
    _name = 'videoclub.director'
    _description = 'videoclub.director'

    nombre = fields.Char(string="Director", help="Director",required=True)
    peliculas_ids = fields.Many2many('videoclub.pelicula',ondelete='cascade',required=True,string='Peliculas')

class pelicula(models.Model):
    _name = 'videoclub.pelicula'
    _description = 'videoclub.pelicula'

    nombre = fields.Char(string="Título", required=True)
    fecha_lanzamiento = fields.Date(string="Fecha de lanzamiento")
    genero_id =  fields.Many2one(string='Género',comodel_name='videoclub.genero',ondelete='set null',help='Género')
    director_id = fields.Many2one(string='Director',comodel_name='videoclub.director',ondelete='set null',help='Director')
    duracion = fields.Integer(string="Duracion")
    precio = fields.Float(string="Precio", help="Precio de alquiler de la película")
    caratula = fields.Image(max_width=310,max_height=420)

    cantidad_disponible = fields.Integer(string="Cantidad disponible", default=0)
    disponible = fields.Boolean(string="Disponible", compute="esta_disponible", store=True)

    # ---------- Funciones ----------

    # establece la cantidad de películas a 0.
    def accion_boton(self):
        for record in self:
            record.write({'cantidad_disponible':0})

    # disponible se establece según la variable cantidad_disponible.
    @api.depends('cantidad_disponible')
    def esta_disponible(self):
        for record in self:
            if record.cantidad_disponible > 0:
                record.disponible = True
            else:
                record.disponible = False


