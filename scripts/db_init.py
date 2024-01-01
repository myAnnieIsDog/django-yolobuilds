from django.core.management import call_command

call_command("check")
call_command("migrate")

call_command("makemigrations", "general")
call_command("migrate")

call_command("makemigrations", "profiles")
call_command("migrate")

call_command("makemigrations", "addresses")
call_command("migrate")

call_command("makemigrations", "fees")
call_command("migrate")

call_command("makemigrations", "permits")
call_command("migrate")

call_command("makemigrations", "payments")
call_command("migrate")

call_command("runscript", "db_initialize")
