from datasette import hookimpl
from datasette.utils.asgi import Response


@hookimpl
def register_routes():
    return (
        (
            r"^/til/til/(?P<topic>[^_]+)_(?P<slug>[^\.]+)\.md$",
            lambda request: Response.redirect(
                "/{topic}/{slug}".format(**request.url_vars), status=301
            ),
        ),
        ("^/til/feed.atom$", lambda: Response.redirect("/scratch/feed.atom", status=301)),
        (
            "^/til$",
            lambda request: Response.redirect(
                "/scratch"
                + (("?" + request.query_string) if request.query_string else ""),
                status=301,
            ),
        ),
        (
            "^/til/search$",
            lambda request: Response.redirect(
                "/scratch/search"
                + (("?" + request.query_string) if request.query_string else ""),
                status=301,
            ),
        ),
    )
