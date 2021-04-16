# Generated by Django 3.2 on 2021-04-14 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0004_alter_funcionario_empresa'),
        ('documentos', '0002_documento_pertence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='pertence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario'),
        ),
    ]