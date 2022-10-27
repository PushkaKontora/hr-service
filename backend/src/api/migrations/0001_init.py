# Generated by Django 4.1.2 on 2022-10-25 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Competency",
            fields=[
                ("name", models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "competencies",
            },
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=256)),
                ("description", models.TextField()),
            ],
            options={
                "db_table": "departments",
            },
        ),
        migrations.CreateModel(
            name="FavoriteResume",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("added_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "favorite_resumes",
            },
        ),
        migrations.CreateModel(
            name="FavoriteVacancy",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("added_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "favorite_vacancies",
            },
        ),
        migrations.CreateModel(
            name="Resume",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("document", models.FileField(upload_to="resumes/%Y/%m/%d/")),
                ("desired_job", models.CharField(max_length=128)),
                (
                    "experience",
                    models.CharField(
                        choices=[
                            ("no_experience", "No Experience"),
                            ("from_one_to_three_years", "From One To Three Years"),
                            ("from_three_to_six_years", "From Three To Six Years"),
                            ("more_than_six_years", "More Than Six Years"),
                        ],
                        max_length=32,
                        null=True,
                    ),
                ),
                ("desired_salary", models.PositiveIntegerField(null=True)),
                ("published_at", models.DateTimeField(null=True)),
            ],
            options={
                "db_table": "resumes",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("email", models.EmailField(max_length=256, unique=True)),
                (
                    "permission",
                    models.CharField(
                        choices=[("user", "User"), ("employer", "Employer"), ("admin", "Admin")], max_length=32
                    ),
                ),
                ("surname", models.CharField(max_length=128)),
                ("name", models.CharField(max_length=128)),
                ("patronymic", models.CharField(max_length=128)),
                ("photo", models.FileField(null=True, upload_to="photos/%Y/%m/%d/")),
                ("favorite_resumes", models.ManyToManyField(through="api.FavoriteResume", to="api.resume")),
            ],
            options={
                "db_table": "users",
            },
        ),
        migrations.CreateModel(
            name="Vacancy",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=256)),
                ("description", models.TextField()),
                (
                    "expected_experience",
                    models.CharField(
                        choices=[
                            ("no_experience", "No Experience"),
                            ("from_one_to_three_years", "From One To Three Years"),
                            ("from_three_to_six_years", "From Three To Six Years"),
                            ("more_than_six_years", "More Than Six Years"),
                        ],
                        max_length=32,
                        null=True,
                    ),
                ),
                ("salary_from", models.PositiveIntegerField(null=True)),
                ("salary_to", models.PositiveIntegerField(null=True)),
                ("published_at", models.DateTimeField(null=True)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="vacancies", to="api.department"
                    ),
                ),
            ],
            options={
                "db_table": "vacancies",
            },
        ),
        migrations.CreateModel(
            name="VacancyRequest",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.user")),
                ("vacancy", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.vacancy")),
            ],
            options={
                "db_table": "vacancies_requests",
            },
        ),
        migrations.AddField(
            model_name="user",
            name="favorite_vacancies",
            field=models.ManyToManyField(through="api.FavoriteVacancy", to="api.vacancy"),
        ),
        migrations.CreateModel(
            name="ResumeCompetency",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("competency", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.competency")),
                ("resume", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.resume")),
            ],
            options={
                "db_table": "resumes_competencies",
                "unique_together": {("resume", "competency")},
            },
        ),
        migrations.AddField(
            model_name="resume",
            name="competencies",
            field=models.ManyToManyField(through="api.ResumeCompetency", to="api.competency"),
        ),
        migrations.AddField(
            model_name="resume",
            name="owner",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, related_name="resume", to="api.user"
            ),
        ),
        migrations.CreateModel(
            name="Password",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("value", models.CharField(max_length=512)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "owner",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, related_name="password", to="api.user"
                    ),
                ),
            ],
            options={
                "db_table": "passwords",
            },
        ),
        migrations.CreateModel(
            name="IssuedToken",
            fields=[
                ("value", models.CharField(max_length=512, primary_key=True, serialize=False)),
                ("revoked", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="issued_tokens", to="api.user"
                    ),
                ),
            ],
            options={
                "db_table": "issued_tokens",
            },
        ),
        migrations.AddField(
            model_name="favoritevacancy",
            name="user",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.user"),
        ),
        migrations.AddField(
            model_name="favoritevacancy",
            name="vacancy",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.vacancy"),
        ),
        migrations.AddField(
            model_name="favoriteresume",
            name="resume",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.resume"),
        ),
        migrations.AddField(
            model_name="favoriteresume",
            name="user",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.user"),
        ),
        migrations.AddField(
            model_name="department",
            name="leader",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT, related_name="department", to="api.user"
            ),
        ),
    ]
