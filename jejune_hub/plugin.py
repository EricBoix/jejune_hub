"""Jejune hub plugin entry-point."""

import os
import urllib.error
import urllib.request

import click

from jejune_cli.plugin_description import PluginDescription

from .component_cont_hub import CompHub

_DEFAULT_PORT = "8776"
_CONFIG_VAR = "HUB_PORT"

_component = CompHub()


def _check_availability() -> tuple[bool, str]:
    if not _component.is_running()[0]:
        return False, "container not running"
    port = os.environ.get(_CONFIG_VAR, _DEFAULT_PORT)
    url = f"http://localhost:{port}/"
    try:
        urllib.request.urlopen(url, timeout=2)
        return True, f"responding on :{port}"
    except urllib.error.URLError as exc:
        return False, str(exc.reason)
    except Exception as exc:
        return False, str(exc)


@click.group("hub")
def hub_group():
    """Commands for the jejune hub UI component."""


@hub_group.command("status-availability")
def status_availability():
    """Show hub availability status (mirrors the doctor Status column)."""
    ok, _ = _check_availability()
    if ok:
        click.echo(f"hub: {click.style('ok', fg='green')}")
    else:
        click.echo(f"hub: {click.style('error', fg='red')}")


@hub_group.command("hint-availability")
def hint_availability():
    """Show how to start the hub container."""
    ok, _ = _check_availability()
    if ok:
        click.echo(click.style("hub is reachable", fg="green"))
    else:
        click.echo("run `docker compose --env-file deployment.env up -d`")


plugin = PluginDescription(
    name="hub",
    group=hub_group,
    config_vars=[_CONFIG_VAR],
    config_hint=(
        f"Set {_CONFIG_VAR} in deployment.env (in the deployment directory)"
        f" to the port exposed by the hub container (default {_DEFAULT_PORT})."
    ),
    avail_hint="",
    check_availability=_check_availability,
    target_role="deployer",
    component=_component,
    repo_name="jejune_hub",
)
