import typer
import job_cli.commands.fetch.fetch as commands_fetch


CONTEXT_SETTINGS = {"allow_extra_args": True}

app = typer.Typer(help="🔍 CLI pour récupérer les offres d'emploi via l'API France Travail.")

fetch_app = typer.Typer()
app.add_typer(fetch_app, name="fetch")
fetch_app.command('job', context_settings=CONTEXT_SETTINGS)(commands_fetch.fetch_job)


if __name__ == "__main__":
    app()
