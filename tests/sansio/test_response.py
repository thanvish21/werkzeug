from werkzeug.sansio.response import Response


def test_location_iri_to_uri() -> None:
    resp = Response()
    # When accessed directly from headers, the location is a URI
    resp.location = "http://üser:pässword@☃.net/påth"
    assert (
        resp.headers["Location"]
        == "http://%C3%BCser:p%C3%A4ssword@xn--n3h.net/p%C3%A5th"
    )
    # When accessed via the property, the location is an IRI
    assert resp.location == "http://üser:pässword@☃.net/påth"

    resp.content_location = "http://☃.net/"
    assert resp.headers["Content-Location"] == "http://xn--n3h.net/"
    assert resp.content_location == "http://☃.net/"


def test_location_unset() -> None:
    resp = Response()
    resp.location = "/test"
    assert "Location" in resp.headers
    resp.location = None
    assert "Location" not in resp.headers
    assert resp.location is None

    resp.content_location = "/test"
    assert "Content-Location" in resp.headers
    del resp.content_location
    assert "Content-Location" not in resp.headers
    assert resp.content_location is None
