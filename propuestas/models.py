from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Direccion(models.Model):
    direccion=models.CharField(max_length=150)

    alt_region=(
        (1, 'Región de Arica y Parinacota'),
        (2, 'Región de Tarapacá'),
        (3, 'Región de Antofagasta'),
        (4, 'Región de Atacama'),
        (5, 'Región de Coquimbo'),
        (6, 'Región de Valparaíso'),
        (7, 'Región Metropolitana'),
        (8, 'Región del Libertador General Bernardo OHiggins'),
        (9, 'Región del Maule'),
        (10, 'Región de Ñuble'),
        (11, 'Región del Biobío'),
        (12, 'Región de La Araucanía'),
        (13, 'Región de Los Ríos'),
        (14, 'Región de Los Lagos'),
        (15, 'Región de Aysén del General Carlos Ibáñez del Campo'),
        (16, 'Región de Magallanes y de la Antártica Chilena')
    )

    region=models.IntegerField(choices=alt_region)
    ciudad=models.CharField(max_length=25)

    alt_comuna=(
        (1, 'Arica'),
        (2, 'Camarones'),
        (3, 'Iquique'),
        (4, 'Pica'),
        (5, 'Pozo Almonte'),
        (6, 'Huara'),
        (7, 'Camina'),
        (8, 'Colchane'),
        (9, 'Alto Hospicio'),
        (10, 'Putre'),
        (11, 'General Lagos'),
        (12, 'Tocopilla'),
        (13, 'Maria Elena'),
        (14, 'Antofagasta'),
        (15, 'Taltal'),
        (16, 'Mejillones'),
        (17, 'Sierra Gorda'),
        (18, 'Calama'),
        (19, 'Ollague'),
        (20, 'San Pedro De Atacama'),
        (21, 'Chanaral'),
        (22, 'Diego De Almagro'),
        (23, 'Copiapo'),
        (24, 'Caldera'),
        (25, 'Tierra Amarilla'),
        (26, 'Vallenar'),
        (27, 'Freirina'),
        (28, 'Huasco'),
        (29, 'Alto Del Carmen'),
        (30, 'La Serena'),
        (31, 'La Higuera'),
        (32, 'Coquimbo'),
        (33, 'Andacollo'),
        (34, 'Vicuna'),
        (35, 'Paihuano'),
        (36, 'Ovalle'),
        (37, 'Monte Patria'),
        (38, 'Punitaqui'),
        (39, 'Combarbala'),
        (40, 'Rio Hurtado'),
        (41, 'Illapel'),
        (42, 'Salamanca'),
        (43, 'Los Vilos'),
        (44, 'Canela'),
        (45, 'Isla De Pascua'),
        (46, 'La Ligua'),
        (47, 'Petorca'),
        (48, 'Cabildo'),
        (49, 'Zapallar'),
        (50, 'Papudo'),
        (51, 'Valparaiso'),
        (52, 'Vina Del Mar'),
        (53, 'Villa Alemana'),
        (54, 'Quilpue'),
        (55, 'Casablanca'),
        (56, 'Quintero'),
        (57, 'Puchuncavi'),
        (58, 'Juan Fernandez'),
        (59, 'Concon'),
        (60, 'San Antonio'),
        (61, 'Santo Domingo'),
        (62, 'Cartagena'),
        (63, 'El Tabo'),
        (64, 'El Quisco'),
        (65, 'Algarrobo'),
        (66, 'Quillota'),
        (67, 'Nogales'),
        (68, 'Hijuelas'),
        (69, 'La Calera'),
        (70, 'La Cruz'),
        (71, 'Limache'),
        (72, 'Olmue'),
        (73, 'San Felipe'),
        (74, 'Panquehue'),
        (75, 'Catemu'),
        (76, 'Putaendo'),
        (77, 'Santa Maria'),
        (78, 'Llay-Llay'),
        (79, 'Los Andes'),
        (80, 'Calle Larga'),
        (81, 'San Esteban'),
        (82, 'Rinconada'),
        (83, 'Rancagua'),
        (84, 'Machali'),
        (85, 'Graneros'),
        (86, 'San Francisco De Mostazal'),
        (87, 'Donihue'),
        (88, 'Coltauco'),
        (89, 'Codegua'),
        (90, 'Peumo'),
        (91, 'Las Cabras'),
        (92, 'San Vicente'),
        (93, 'Pichidegua'),
        (94, 'Rengo'),
        (95, 'Requinoa'),
        (96, 'Olivar'),
        (97, 'Malloa'),
        (98, 'Coinco'),
        (99, 'Quinta De Tilcoco'),
        (100, 'San Fernando'),
        (101, 'Chimbarongo'),
        (102, 'Nancagua'),
        (103, 'Placilla'),
        (104, 'Santa Cruz'),
        (105, 'Lolol'),
        (106, 'Palmilla'),
        (107, 'Peralillo'),
        (108, 'Chepica'),
        (109, 'Pumanque'),
        (110, 'Pichilemu'),
        (111, 'Navidad'),
        (112, 'Litueche'),
        (113, 'La Estrella'),
        (114, 'Marchigue'),
        (115, 'Paredones'),
        (116, 'Curico'),
        (117, 'Teno'),
        (118, 'Romeral'),
        (119, 'Rauco'),
        (120, 'Licanten'),
        (121, 'Vichuquen'),
        (122, 'Hualane'),
        (123, 'Molina'),
        (124, 'Sagrada Familia'),
        (125, 'Talca'),
        (126, 'San Clemente'),
        (127, 'Pelarco'),
        (128, 'Rio Claro'),
        (129, 'Pencahue'),
        (130, 'Maule'),
        (131, 'Curepto'),
        (132, 'Constitucion'),
        (133, 'Empedrado'),
        (134, 'San Rafael'),
        (135, 'Linares'),
        (136, 'Yerbas Buenas'),
        (137, 'Colbun'),
        (138, 'Longavi'),
        (139, 'Parral'),
        (140, 'Retiro'),
        (141, 'Villa Alegre'),
        (142, 'San Javier'),
        (143, 'Cauquenes'),
        (144, 'Pelluhue'),
        (145, 'Chanco'),
        (146, 'Chillan'),
        (147, 'Pinto'),
        (148, 'Coihueco'),
        (149, 'Quirihue'),
        (150, 'Ninhue'),
        (151, 'Portezuelo'),
        (152, 'Cobquecura'),
        (153, 'Trehuaco'),
        (154, 'San Carlos'),
        (155, 'Niquen'),
        (156, 'San Fabian'),
        (157, 'San Nicolas'),
        (158, 'Bulnes'),
        (159, 'San Ignacio'),
        (160, 'Quillon'),
        (161, 'Yungay'),
        (162, 'Pemuco'),
        (163, 'El Carmen'),
        (164, 'Ranquil'),
        (165, 'Coelemu'),
        (166, 'Chillan Viejo'),
        (167, 'Concepcion'),
        (168, 'Penco'),
        (169, 'Hualqui'),
        (170, 'Florida'),
        (171, 'Tome'),
        (172, 'Talcahuano'),
        (173, 'Coronel'),
        (174, 'Lota'),
        (175, 'Santa Juana'),
        (176, 'San Pedro De La Paz'),
        (177, 'Chiguayante'),
        (178, 'Hualpen'),
        (179, 'Arauco'),
        (180, 'Curanilahue'),
        (181, 'Lebu'),
        (182, 'Los Alamos'),
        (183, 'Canete'),
        (184, 'Contulmo'),
        (185, 'Tirua'),
        (186, 'Los Angeles'),
        (187, 'Santa Barbara'),
        (188, 'Laja'),
        (189, 'Quilleco'),
        (190, 'Nacimiento'),
        (191, 'Negrete'),
        (192, 'Mulchen'),
        (193, 'Quilaco'),
        (194, 'Yumbel'),
        (195, 'Cabrero'),
        (196, 'San Rosendo'),
        (197, 'Tucapel'),
        (198, 'Antuco'),
        (199, 'Alto Biobio'),
        (200, 'Angol'),
        (201, 'Puren'),
        (202, 'Los Sauces'),
        (203, 'Renaico'),
        (204, 'Collipulli'),
        (205, 'Ercilla'),
        (206, 'Traiguen'),
        (207, 'Lumaco'),
        (208, 'Victoria'),
        (209, 'Curacautin'),
        (210, 'Lonquimay'),
        (211, 'Temuco'),
        (212, 'Vilcun'),
        (213, 'Freire'),
        (214, 'Cunco'),
        (215, 'Lautaro'),
        (216, 'Perquenco'),
        (217, 'Galvarino'),
        (218, 'Nueva Imperial'),
        (219, 'Carahue'),
        (220, 'Saavedra'),
        (221, 'Pitrufquen'),
        (222, 'Gorbea'),
        (223, 'Tolten'),
        (224, 'Loncoche'),
        (225, 'Villarrica'),
        (226, 'Pucon'),
        (227, 'Melipeuco'),
        (228, 'Curarrehue'),
        (229, 'Teodoro Schmidt'),
        (230, 'Padre Las Casas'),
        (231, 'Cholchol'),
        (232, 'Valdivia'),
        (233, 'Mariquina'),
        (234, 'Lanco'),
        (235, 'Los Lagos'),
        (236, 'Futrono'),
        (237, 'Corral'),
        (238, 'Mafil'),
        (239, 'Panguipulli'),
        (240, 'La Union'),
        (241, 'Paillaco'),
        (242, 'Rio Bueno'),
        (243, 'Lago Ranco'),
        (244, 'Osorno'),
        (245, 'San Pablo'),
        (246, 'Puerto Octay'),
        (247, 'Puyehue'),
        (248, 'Rio Negro'),
        (249, 'Purranque'),
        (250, 'San Juan De La Costa'),
        (251, 'Puerto Montt'),
        (252, 'Cochamo'),
        (253, 'Puerto Varas'),
        (254, 'Fresia'),
        (255, 'Frutillar'),
        (256, 'Llanquihue'),
        (257, 'Maullin'),
        (258, 'Los Muermos'),
        (259, 'Calbuco'),
        (260, 'Castro'),
        (261, 'Chonchi'),
        (262, 'Queilen'),
        (263, 'Quellon'),
        (264, 'Puqueldon'),
        (265, 'Ancud'),
        (266, 'Quemchi'),
        (267, 'Dalcahue'),
        (268, 'Curaco De Velez'),
        (269, 'Quinchao'),
        (270, 'Chaiten'),
        (271, 'Hualaihue'),
        (272, 'Futaleufu'),
        (273, 'Palena'),
        (274, 'Aysen'),
        (275, 'Cisnes'),
        (276, 'Guaitecas'),
        (277, 'Chile Chico'),
        (278, 'Rio Ibanez'),
        (279, 'Cochrane'),
        (280, 'Ohiggins'),
        (281, 'Tortel'),
        (282, 'Coyhaique'),
        (283, 'Lago Verde'),
        (284, 'Natales'),
        (285, 'Torres Del Paine'),
        (286, 'Rio Verde'),
        (287, 'San Gregorio'),
        (288, 'Punta Arenas'),
        (289, 'Laguna Blanca'),
        (290, 'Porvenir'),
        (291, 'Primavera'),
        (292, 'Timaukel'),
        (293, 'Cabo De Hornos'),
        (294, 'Santiago'),
        (295, 'Santiago Oeste'),
        (296, 'Santiago Sur'),
        (297, 'Recoleta'),
        (298, 'Independencia'),
        (299, 'Quinta Normal'),
        (300, 'Maipu'),
        (301, 'Pudahuel'),
        (302, 'Renca'),
        (303, 'Quilicura'),
        (304, 'Conchali'),
        (305, 'Lo Prado'),
        (306, 'Cerro Navia'),
        (307, 'Estacion Central'),
        (308, 'Huechuraba'),
        (309, 'Cerrillos'),
        (310, 'Colina'),
        (311, 'Lampa'),
        (312, 'Til-Til'),
        (313, 'Talagante'),
        (314, 'Isla De Maipo'),
        (315, 'El Monte'),
        (316, 'Penaflor'),
        (317, 'Padre Hurtado'),
        (318, 'Melipilla'),
        (319, 'Maria Pinto'),
        (320, 'Curacavi'),
        (321, 'San Pedro'),
        (322, 'Alhue'),
        (323, 'Providencia'),
        (324, 'Nunoa'),
        (325, 'Las Condes'),
        (326, 'La Florida'),
        (327, 'La Reina'),
        (328, 'Macul'),
        (329, 'Penalolen'),
        (330, 'Vitacura'),
        (331, 'Lo Barnechea'),
        (332, 'San Miguel'),
        (333, 'La Cisterna'),
        (334, 'La Granja'),
        (335, 'San Ramon'),
        (336, 'La Pintana'),
        (337, 'Pedro Aguirre Cerda'),
        (338, 'San Joaquin'),
        (339, 'Lo Espejo'),
        (340, 'El Bosque'),
        (341, 'Puente Alto'),
        (342, 'Pirque'),
        (343, 'San Jose De Maipo'),
        (344, 'San Bernardo'),
        (345, 'Calera De Tango'),
        (346, 'Buin'),
        (347, 'Paine'),
    )
    
    comuna=models.IntegerField(choices=alt_comuna, default='')
    ultima_mod=models.DateTimeField(auto_now=True)
    creado=models.DateTimeField(auto_now_add=True)

class Cliente(models.Model):
    
    alt_pers=(
        (1, 'Persona Natural'),
        (2, 'Empresa')
    )
    
    tipo_pers=models.IntegerField(choices=alt_pers, default='')
    razon_social=models.CharField(max_length=50, blank=True, null=True)
    nombres=models.CharField(max_length=50, blank=True, null=True)
    ape_pat=models.CharField(max_length=50, blank=True, null=True)
    ape_mat=models.CharField(max_length=50, blank=True, null=True)
    rut=models.CharField(max_length=12, primary_key = True)
    direccion=models.OneToOneField(Direccion, default='', on_delete=models.CASCADE)
    email=models.EmailField(blank=True, null=True)
    telefono=models.CharField(max_length=12, blank=True, null=True)
    celular=models.CharField(max_length=12, blank=True, null=True)
    activo=models.BooleanField(blank=True, null=True, default=True)
    ultima_mod=models.DateTimeField(auto_now=True)
    creado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'

    def personeria(self, *args, **kwargs):
        if self.tipo_pers == 2:
            return self.razon_social
        else:
            return self.nombres, self.ape_pat, self.ape_mat
            
    
       





class Corredor(models.Model):
    razon_social=models.CharField(max_length=50)
    rut=models.CharField(max_length=12, primary_key = True)
    direccion=models.OneToOneField(Direccion, default='', on_delete=models.CASCADE)
    ultima_mod=models.DateTimeField(auto_now=True)
    creado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Corredor'
        verbose_name_plural='Corredores'


class Compania(models.Model):
    nombre=models.CharField(max_length=50)
    ejecutivo=models.CharField(max_length=50)
    email=models.EmailField(blank=True, null=True)
    telefono=models.CharField(max_length=12, blank=True, null=True)
    ultima_mod=models.DateTimeField(auto_now=True)
    creado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Compañía'
        verbose_name_plural='Compañías'


class Ramo(models.Model):
    ramo=models.CharField(max_length=25)
    com_afe=models.IntegerField(default=10)
    com_exe=models.IntegerField(default=0)
    deducible=models.IntegerField(default=0)
    ultima_mod=models.DateTimeField(auto_now=True)
    creado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Ramo'
        verbose_name_plural='Ramos'



class Riesgo(models.Model):
    tipo=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    ano=models.CharField(max_length=50, verbose_name='Año')
    patente=models.CharField(max_length=6)
    nro_motor=models.CharField(max_length=25, blank=True, null=True)
    nro_chasis=models.CharField(max_length=25, blank=True, null=True)
    prima_neta=models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    ultima_mod=models.DateTimeField(auto_now=True)
    creado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Riesgo'
        verbose_name_plural='Riesgos'

class Plan_Pago(models.Model):
    
    alt_medio_pago=(
        (1, 'Contado'),
        (2, 'Aviso de Vencimiento'),
        (3, 'PAC'),
        (4, 'PAT'),
    )

    medio_pago=models.IntegerField(choices=alt_medio_pago, default='')
    
    alt_cuotas=(
        (1, '1 Cuota'),
        (2, '2 Cuotas'),
        (3, '3 Cuotas'),
        (4, '4 Cuotas'),
        (5, '5 Cuotas'),
        (6, '6 Cuotas'),
        (7, '7 Cuotas'),
        (8, '8 Cuotas'),
        (9, '9 Cuotas'),
        (10, '10 Cuotas'),
        (11, '11 Cuotas'),
        (12, '12 Cuotas'),
    )

    cuotas=models.IntegerField(choices=alt_cuotas, default='')
    interes=models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    ultima_mod=models.DateTimeField(auto_now=True)
    creado=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='Plan de Pago'
        verbose_name_plural='Planes de Pago'


class Propuesta(models.Model):
    id_propuesta=models.AutoField(primary_key=True)
    corredor=models.OneToOneField(Corredor, default='', on_delete=models.CASCADE)
    compania=models.OneToOneField(Compania, default='', on_delete=models.CASCADE, verbose_name='Compañía')
    cliente=models.ForeignKey(Cliente, default='', on_delete=models.CASCADE)
    fecha_propuesta=models.DateField(blank=False, null=False)
    inicio_vigencia=models.DateField(blank=False, null=False)
    fin_vigencia=models.DateField(blank=False, null=False)
    d_vigencia=models.IntegerField(default=0)
    d_exclu=models.IntegerField(default=0)
    renu_poliza=models.CharField(max_length=25, blank=True, null=True)
    endoso=models.CharField(max_length=25, blank=True, null=True)
    ramo=models.OneToOneField(Ramo, default='', on_delete=models.CASCADE)
    riesgo=models.ManyToManyField(Riesgo, default='')
    minuta=models.TextField(max_length=500, blank=True, null=True)
    plan_pago=models.OneToOneField(Plan_Pago, default='', on_delete=models.CASCADE)
    ultima_mod=models.DateTimeField(auto_now=True)
    creado=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name='Propuesta'
        verbose_name_plural='Propuestas'





class Prima(models.Model):
    id_prima=models.AutoField(primary_key=True)
    prima_afecta=models.DecimalField(max_digits=5, decimal_places=2)
    prima_exenta=models.DecimalField(max_digits=5, decimal_places=2)
    prima_neta=models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    prima_bruta=models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    ultima_mod=models.DateTimeField(auto_now=True)
    creado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Prima'
        verbose_name_plural='Primas'

#    def prima_bruta_calc (self):
#        if self.prima_exenta == 0:
#            return self.prima_afecta * 1.19
#       else:
#            return self.prima_afecta * 1.19 + self.prima_exenta