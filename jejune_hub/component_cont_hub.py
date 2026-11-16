"""Hub containerized component."""

from pathlib import Path

from jejune_cli.core.component_containerized import ContComp
from jejune_cli.core.containerized_context import ContainerizedContext


class CompHub(ContComp):
    def __init__(self, context: ContainerizedContext) -> None:
        super().__init__(
            name="hub",
            image_name="jejune:hub",
            dockerfile="DockerContext/Dockerfile",
            service_name="hub",
            hint="run `jejune build`",
            context=context,
        )
        self.repos = [(None, "HUB_CONTEXT")]
        if self._context.ecosystem is not None:
            self.conditional_dependencies = [
                (lambda: not self.is_available(), self._context.ecosystem)
            ]

    def is_available(self) -> bool:
        return self.is_built()

    def is_running(self) -> tuple[bool, str]:
        deploy_name = Path(".").resolve().name.lower()
        return super().is_running(f"jejune-{deploy_name}-{self.service_name}-1")
