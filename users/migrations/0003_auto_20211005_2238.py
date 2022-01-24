# Generated by Django 3.2.7 on 2021-10-05 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_aplicaciones_allauth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_imagen', models.CharField(max_length=20)),
                ('nombre_a_mostrar', models.CharField(max_length=20)),
                ('descripcion', models.TextField(blank=True, max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='user',
            name='pais',
            field=models.CharField(blank=True, choices=[('Afganistán', 'Afganistán'), ('Albania', 'Albania'), ('Alemania', 'Alemania'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Antigua y Barbuda', 'Antigua y Barbuda'), ('Arabia Saudita', 'Arabia Saudita'), ('Argelia', 'Argelia'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaiyán', 'Azerbaiyán'), ('Bahamas', 'Bahamas'), ('Bangladés', 'Bangladés'), ('Barbados', 'Barbados'), ('Baréin', 'Baréin'), ('Bélgica', 'Bélgica'), ('Belice', 'Belice'), ('Benín', 'Benín'), ('Bielorrusia', 'Bielorrusia'), ('Birmania', 'Birmania'), ('Bolivia', 'Bolivia'), ('Bosnia y Herzegovina', 'Bosnia y Herzegovina'), ('Botsuana', 'Botsuana'), ('Brasil', 'Brasil'), ('Brunéi', 'Brunéi'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Bután', 'Bután'), ('Cabo Verde', 'Cabo Verde'), ('Camboya', 'Camboya'), ('Camerún', 'Camerún'), ('Canadá', 'Canadá'), ('Catar', 'Catar'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Chipre', 'Chipre'), ('Ciudad del Vaticano', 'Ciudad del Vaticano'), ('Colombia', 'Colombia'), ('Comoras', 'Comoras'), ('Corea del Norte', 'Corea del Norte'), ('Corea del Sur', 'Corea del Sur'), ('Costa de Marfil', 'Costa de Marfil'), ('Costa Rica', 'Costa Rica'), ('Croacia', 'Croacia'), ('Cuba', 'Cuba'), ('Dinamarca', 'Dinamarca'), ('Dominica', 'Dominica'), ('Ecuador', 'Ecuador'), ('Egipto', 'Egipto'), ('El Salvador', 'El Salvador'), ('Emiratos Árabes Unidos', 'Emiratos Árabes Unidos'), ('Eritrea', 'Eritrea'), ('Eslovaquia', 'Eslovaquia'), ('Eslovenia', 'Eslovenia'), ('España', 'España'), ('Estados Unidos', 'Estados Unidos'), ('Estonia', 'Estonia'), ('Etiopía', 'Etiopía'), ('Filipinas', 'Filipinas'), ('Finlandia', 'Finlandia'), ('Fiyi', 'Fiyi'), ('Francia', 'Francia'), ('Gabón', 'Gabón'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Ghana', 'Ghana'), ('Granada', 'Granada'), ('Grecia', 'Grecia'), ('Guatemala', 'Guatemala'), ('Guyana', 'Guyana'), ('Guinea', 'Guinea'), ('Guinea ecuatorial', 'Guinea ecuatorial'), ('Guinea-Bisáu', 'Guinea-Bisáu'), ('Haití', 'Haití'), ('Honduras', 'Honduras'), ('Hungría', 'Hungría'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Irak', 'Irak'), ('Irán', 'Irán'), ('Irlanda', 'Irlanda'), ('Islandia', 'Islandia'), ('Islas Marshall', 'Islas Marshall'), ('Islas Salomón', 'Islas Salomón'), ('Israel', 'Israel'), ('Italia', 'Italia'), ('Jamaica', 'Jamaica'), ('Japón', 'Japón'), ('Jordania', 'Jordania'), ('Kazajistán', 'Kazajistán'), ('Kenia', 'Kenia'), ('Kirguistán', 'Kirguistán'), ('Kiribati', 'Kiribati'), ('Kuwait', 'Kuwait'), ('Laos', 'Laos'), ('Lesoto', 'Lesoto'), ('Letonia', 'Letonia'), ('Líbano', 'Líbano'), ('Liberia', 'Liberia'), ('Libia', 'Libia'), ('Liechtenstein', 'Liechtenstein'), ('Lituania', 'Lituania'), ('Luxemburgo', 'Luxemburgo'), ('Macedonia del Norte', 'Macedonia del Norte'), ('Madagascar', 'Madagascar'), ('Malasia', 'Malasia'), ('Malaui', 'Malaui'), ('Maldivas', 'Maldivas'), ('Malí', 'Malí'), ('Malta', 'Malta'), ('Marruecos', 'Marruecos'), ('Mauricio', 'Mauricio'), ('Mauritania', 'Mauritania'), ('México', 'México'), ('Micronesia', 'Micronesia'), ('Moldavia', 'Moldavia'), ('Mónaco', 'Mónaco'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Nicaragua', 'Nicaragua'), ('Níger', 'Níger'), ('Nigeria', 'Nigeria'), ('Noruega', 'Noruega'), ('Nueva Zelanda', 'Nueva Zelanda'), ('Omán', 'Omán'), ('Países Bajos', 'Países Bajos'), ('Pakistán', 'Pakistán'), ('Palaos', 'Palaos'), ('Panamá', 'Panamá'), ('Papúa Nueva Guinea', 'Papúa Nueva Guinea'), ('Paraguay', 'Paraguay'), ('Perú', 'Perú'), ('Polonia', 'Polonia'), ('Portugal', 'Portugal'), ('Reino Unido', 'Reino Unido'), ('República Centroafricana', 'República Centroafricana'), ('República Checa', 'República Checa'), ('República del Congo', 'República del Congo'), ('República Democrática del Congo', 'República Democrática del Congo'), ('República Dominicana', 'República Dominicana'), ('Ruanda', 'Ruanda'), ('Rumanía', 'Rumanía'), ('Rusia', 'Rusia'), ('Samoa', 'Samoa'), ('San Cristóbal y Nieves', 'San Cristóbal y Nieves'), ('San Marino', 'San Marino'), ('San Vicente y las Granadinas', 'San Vicente y las Granadinas'), ('Santa Lucía', 'Santa Lucía'), ('Santo Tomé y Príncipe', 'Santo Tomé y Príncipe'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leona', 'Sierra Leona'), ('Singapur', 'Singapur'), ('Siria', 'Siria'), ('Somalia', 'Somalia'), ('Sri Lanka', 'Sri Lanka'), ('Suazilandia', 'Suazilandia'), ('Sudáfrica', 'Sudáfrica'), ('Sudán', 'Sudán'), ('Sudán del Sur', 'Sudán del Sur'), ('Suecia', 'Suecia'), ('Suiza', 'Suiza'), ('Surinam', 'Surinam'), ('Tailandia', 'Tailandia'), ('Tanzania', 'Tanzania'), ('Tayikistán', 'Tayikistán'), ('Timor Oriental', 'Timor Oriental'), ('Togo', 'Togo'), ('Tonga', 'Tonga'), ('Trinidad y Tobago', 'Trinidad y Tobago'), ('Túnez', 'Túnez'), ('Turkmenistán', 'Turkmenistán'), ('Turquía', 'Turquía'), ('Tuvalu', 'Tuvalu'), ('Ucrania', 'Ucrania'), ('Uganda', 'Uganda'), ('Uruguay', 'Uruguay'), ('Uzbekistán', 'Uzbekistán'), ('Vanuatu', 'Vanuatu'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Yemen', 'Yemen'), ('Yibuti', 'Yibuti'), ('Zambia', 'Zambia'), ('Zimbabue', 'Zimbabue')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.avatar'),
        ),
    ]
