# https://fastapi.tiangolo.com/

[ ![logo](img/icon-white.svg) ](. "FastAPI") FastAPI

[ fastapi/fastapi  ](https://github.com/fastapi/fastapi "Go to repository")

  * FastAPI  [ FastAPI  ](.) Table of contents 
    * Sponsors 
    * Opinions 
    * **Typer** , the FastAPI of CLIs 
    * Requirements 
    * Installation 
    * Example 
      * Create it 
      * Run it 
      * Check it 
      * Interactive API docs 
      * Alternative API docs 
    * Example upgrade 
      * Interactive API docs upgrade 
      * Alternative API docs upgrade 
      * Recap 
    * Performance 
    * Dependencies 
      * `standard` Dependencies 
      * Without `standard` Dependencies 
      * Additional Optional Dependencies 
    * License 
  * [ Features  ](features/)
  * [ Learn  ](learn/)

Learn

    * [ Python Types Intro  ](python-types/)
    * [ Concurrency and async / await  ](async/)
    * [ Environment Variables  ](environment-variables/)
    * [ Virtual Environments  ](virtual-environments/)
    * [ Tutorial - User Guide  ](tutorial/)

Tutorial - User Guide

      * [ First Steps  ](tutorial/first-steps/)
      * [ Path Parameters  ](tutorial/path-params/)
      * [ Query Parameters  ](tutorial/query-params/)
      * [ Request Body  ](tutorial/body/)
      * [ Query Parameters and String Validations  ](tutorial/query-params-str-validations/)
      * [ Path Parameters and Numeric Validations  ](tutorial/path-params-numeric-validations/)
      * [ Query Parameter Models  ](tutorial/query-param-models/)
      * [ Body - Multiple Parameters  ](tutorial/body-multiple-params/)
      * [ Body - Fields  ](tutorial/body-fields/)
      * [ Body - Nested Models  ](tutorial/body-nested-models/)
      * [ Declare Request Example Data  ](tutorial/schema-extra-example/)
      * [ Extra Data Types  ](tutorial/extra-data-types/)
      * [ Cookie Parameters  ](tutorial/cookie-params/)
      * [ Header Parameters  ](tutorial/header-params/)
      * [ Cookie Parameter Models  ](tutorial/cookie-param-models/)
      * [ Header Parameter Models  ](tutorial/header-param-models/)
      * [ Response Model - Return Type  ](tutorial/response-model/)
      * [ Extra Models  ](tutorial/extra-models/)
      * [ Response Status Code  ](tutorial/response-status-code/)
      * [ Form Data  ](tutorial/request-forms/)
      * [ Form Models  ](tutorial/request-form-models/)
      * [ Request Files  ](tutorial/request-files/)
      * [ Request Forms and Files  ](tutorial/request-forms-and-files/)
      * [ Handling Errors  ](tutorial/handling-errors/)
      * [ Path Operation Configuration  ](tutorial/path-operation-configuration/)
      * [ JSON Compatible Encoder  ](tutorial/encoder/)
      * [ Body - Updates  ](tutorial/body-updates/)
      * [ Dependencies  ](tutorial/dependencies/)

Dependencies

        * [ Classes as Dependencies  ](tutorial/dependencies/classes-as-dependencies/)
        * [ Sub-dependencies  ](tutorial/dependencies/sub-dependencies/)
        * [ Dependencies in path operation decorators  ](tutorial/dependencies/dependencies-in-path-operation-decorators/)
        * [ Global Dependencies  ](tutorial/dependencies/global-dependencies/)
        * [ Dependencies with yield  ](tutorial/dependencies/dependencies-with-yield/)
      * [ Security  ](tutorial/security/)

Security

        * [ Security - First Steps  ](tutorial/security/first-steps/)
        * [ Get Current User  ](tutorial/security/get-current-user/)
        * [ Simple OAuth2 with Password and Bearer  ](tutorial/security/simple-oauth2/)
        * [ OAuth2 with Password (and hashing), Bearer with JWT tokens  ](tutorial/security/oauth2-jwt/)
      * [ Middleware  ](tutorial/middleware/)
      * [ CORS (Cross-Origin Resource Sharing)  ](tutorial/cors/)
      * [ SQL (Relational) Databases  ](tutorial/sql-databases/)
      * [ Bigger Applications - Multiple Files  ](tutorial/bigger-applications/)
      * [ Background Tasks  ](tutorial/background-tasks/)
      * [ Metadata and Docs URLs  ](tutorial/metadata/)
      * [ Static Files  ](tutorial/static-files/)
      * [ Testing  ](tutorial/testing/)
      * [ Debugging  ](tutorial/debugging/)
    * [ Advanced User Guide  ](advanced/)

Advanced User Guide

      * [ Path Operation Advanced Configuration  ](advanced/path-operation-advanced-configuration/)
      * [ Additional Status Codes  ](advanced/additional-status-codes/)
      * [ Return a Response Directly  ](advanced/response-directly/)
      * [ Custom Response - HTML, Stream, File, others  ](advanced/custom-response/)
      * [ Additional Responses in OpenAPI  ](advanced/additional-responses/)
      * [ Response Cookies  ](advanced/response-cookies/)
      * [ Response Headers  ](advanced/response-headers/)
      * [ Response - Change Status Code  ](advanced/response-change-status-code/)
      * [ Advanced Dependencies  ](advanced/advanced-dependencies/)
      * [ Advanced Security  ](advanced/security/)

Advanced Security

        * [ OAuth2 scopes  ](advanced/security/oauth2-scopes/)
        * [ HTTP Basic Auth  ](advanced/security/http-basic-auth/)
      * [ Using the Request Directly  ](advanced/using-request-directly/)
      * [ Using Dataclasses  ](advanced/dataclasses/)
      * [ Advanced Middleware  ](advanced/middleware/)
      * [ Sub Applications - Mounts  ](advanced/sub-applications/)
      * [ Behind a Proxy  ](advanced/behind-a-proxy/)
      * [ Templates  ](advanced/templates/)
      * [ WebSockets  ](advanced/websockets/)
      * [ Lifespan Events  ](advanced/events/)
      * [ Testing WebSockets  ](advanced/testing-websockets/)
      * [ Testing Events: startup - shutdown  ](advanced/testing-events/)
      * [ Testing Dependencies with Overrides  ](advanced/testing-dependencies/)
      * [ Async Tests  ](advanced/async-tests/)
      * [ Settings and Environment Variables  ](advanced/settings/)
      * [ OpenAPI Callbacks  ](advanced/openapi-callbacks/)
      * [ OpenAPI Webhooks  ](advanced/openapi-webhooks/)
      * [ Including WSGI - Flask, Django, others  ](advanced/wsgi/)
      * [ Generate Clients  ](advanced/generate-clients/)
    * [ FastAPI CLI  ](fastapi-cli/)
    * [ Deployment  ](deployment/)

Deployment

      * [ About FastAPI versions  ](deployment/versions/)
      * [ About HTTPS  ](deployment/https/)
      * [ Run a Server Manually  ](deployment/manually/)
      * [ Deployments Concepts  ](deployment/concepts/)
      * [ Deploy FastAPI on Cloud Providers  ](deployment/cloud/)
      * [ Server Workers - Uvicorn with Workers  ](deployment/server-workers/)
      * [ FastAPI in Containers - Docker  ](deployment/docker/)
    * [ How To - Recipes  ](how-to/)

How To - Recipes

      * [ General - How To - Recipes  ](how-to/general/)
      * [ GraphQL  ](how-to/graphql/)
      * [ Custom Request and APIRoute class  ](how-to/custom-request-and-route/)
      * [ Conditional OpenAPI  ](how-to/conditional-openapi/)
      * [ Extending OpenAPI  ](how-to/extending-openapi/)
      * [ Separate OpenAPI Schemas for Input and Output or Not  ](how-to/separate-openapi-schemas/)
      * [ Custom Docs UI Static Assets (Self-Hosting)  ](how-to/custom-docs-ui-assets/)
      * [ Configure Swagger UI  ](how-to/configure-swagger-ui/)
      * [ Testing a Database  ](how-to/testing-database/)
  * [ Reference  ](reference/)

Reference

    * [ `FastAPI` class  ](reference/fastapi/)
    * [ Request Parameters  ](reference/parameters/)
    * [ Status Codes  ](reference/status/)
    * [ `UploadFile` class  ](reference/uploadfile/)
    * [ Exceptions - `HTTPException` and `WebSocketException` ](reference/exceptions/)
    * [ Dependencies - `Depends()` and `Security()` ](reference/dependencies/)
    * [ `APIRouter` class  ](reference/apirouter/)
    * [ Background Tasks - `BackgroundTasks` ](reference/background/)
    * [ `Request` class  ](reference/request/)
    * [ WebSockets  ](reference/websockets/)
    * [ `HTTPConnection` class  ](reference/httpconnection/)
    * [ `Response` class  ](reference/response/)
    * [ Custom Response Classes - File, HTML, Redirect, Streaming, etc.  ](reference/responses/)
    * [ Middleware  ](reference/middleware/)
    * [ OpenAPI  ](reference/openapi/)

OpenAPI

      * [ OpenAPI `docs` ](reference/openapi/docs/)
      * [ OpenAPI `models` ](reference/openapi/models/)
    * [ Security Tools  ](reference/security/)
    * [ Encoders - `jsonable_encoder` ](reference/encoders/)
    * [ Static Files - `StaticFiles` ](reference/staticfiles/)
    * [ Templating - `Jinja2Templates` ](reference/templating/)
    * [ Test Client - `TestClient` ](reference/testclient/)
  * [ FastAPI People  ](fastapi-people/)
  * [ Resources  ](resources/)

Resources

    * [ Help FastAPI - Get Help  ](help-fastapi/)
    * [ Development - Contributing  ](contributing/)
    * [ Full Stack FastAPI Template  ](project-generation/)
    * [ External Links and Articles  ](external-links/)
    * [ FastAPI and friends newsletter  ](newsletter/)
    * [ Repository Management Tasks  ](management-tasks/)
  * [ About  ](about/)

About

    * [ Alternatives, Inspiration and Comparisons  ](alternatives/)
    * [ History, Design and Future  ](history-design-future/)
    * [ Benchmarks  ](benchmarks/)
    * [ Repository Management  ](management/)
  * [ Release Notes  ](release-notes/)

Table of contents

  * Sponsors 
  * Opinions 
  * **Typer** , the FastAPI of CLIs 
  * Requirements 
  * Installation 
  * Example 
    * Create it 
    * Run it 
    * Check it 
    * Interactive API docs 
    * Alternative API docs 
  * Example upgrade 
    * Interactive API docs upgrade 
    * Alternative API docs upgrade 
    * Recap 
  * Performance 
  * Dependencies 
    * `standard` Dependencies 
    * Without `standard` Dependencies 
    * Additional Optional Dependencies 
  * License 

# FastAPI¶

[![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-
teal.png)](https://fastapi.tiangolo.com)

_FastAPI framework, high performance, easy to learn, fast to code, ready for
production_

[
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master)
](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)
[ ![Coverage](https://coverage-
badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ](https://coverage-
badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi) [ ![Package
version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)
](https://pypi.org/project/fastapi) [ ![Supported Python
versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
](https://pypi.org/project/fastapi)

* * *

**Documentation** : <https://fastapi.tiangolo.com>

**Source Code** : <https://github.com/fastapi/fastapi>

* * *

FastAPI is a modern, fast (high-performance), web framework for building APIs
with Python based on standard Python type hints.

The key features are:

  * **Fast** : Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
  * **Fast to code** : Increase the speed to develop features by about 200% to 300%. *
  * **Fewer bugs** : Reduce about 40% of human (developer) induced errors. *
  * **Intuitive** : Great editor support. Completion everywhere. Less time debugging.
  * **Easy** : Designed to be easy to use and learn. Less time reading docs.
  * **Short** : Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
  * **Robust** : Get production-ready code. With automatic interactive documentation.
  * **Standards-based** : Based on (and fully compatible with) the open standards for APIs: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (previously known as Swagger) and [JSON Schema](https://json-schema.org/).

* estimation based on tests on an internal development team, building production applications.

## Sponsors¶

[![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io?ref=fastapi
"BlockBee Cryptocurrency Payment Gateway")
[![](https://fastapi.tiangolo.com/img/sponsors/platform-
sh.png)](https://platform.sh/try-it-now/?utm_source=fastapi-
signup&utm_medium=banner&utm_campaign=FastAPI-signup-June-2023 "Build, run and
scale your apps on a modern, reliable, and secure PaaS.")
[![](https://fastapi.tiangolo.com/img/sponsors/porter.png)](https://www.porter.run
"Deploy FastAPI on AWS with a few clicks")
[![](https://fastapi.tiangolo.com/img/sponsors/bump-
sh.svg)](https://bump.sh/fastapi?utm_source=fastapi&utm_medium=referral&utm_campaign=sponsor
"Automate FastAPI documentation generation with Bump.sh")
[![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-
badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI
files")
[![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge
"Auth, user management and more for your B2B product")
[![](https://fastapi.tiangolo.com/img/sponsors/coherence.png)](https://www.withcoherence.com/?utm_medium=advertising&utm_source=fastapi&utm_campaign=website
"Coherence")
[![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png)](https://www.mongodb.com/developer/languages/python/python-
quickstart-
fastapi/?utm_campaign=fastapi_framework&utm_source=fastapi_sponsorship&utm_medium=web_referral
"Simplify Full Stack Development with FastAPI & MongoDB")
[![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-
gh "Zuplo: Scale, Protect, Document, and Monetize your FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com?utm_source=fastapi
"liblab - Generate SDKs from FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-
fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy
& scale any full-stack web app on Render. Focus on building apps, not infra.")
[![](https://fastapi.tiangolo.com/img/sponsors/haystack-
fastapi.svg)](https://github.com/deepset-ai/haystack/ "Build powerful search
from composable, open source building blocks")
[![](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/
"Pay as you go for market data")
[![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com?utm_source=fastapi+repo&utm_medium=github+sponsorship
"SDKs for your API | Speakeasy")
[![](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/
"Svix - Webhooks as a service")
[![](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral
"Stainless | Generate best-in-class SDKs")

[Other sponsors](https://fastapi.tiangolo.com/fastapi-people/#sponsors)

## Opinions¶

" _[...] I'm using **FastAPI** a ton these days. [...] I'm actually planning
to use it for all of my team's **ML services at Microsoft**. Some of them are
getting integrated into the core **Windows** product and some **Office**
products._"

Kabir Khan - **Microsoft** [(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

" _We adopted the **FastAPI** library to spawn a **REST** server that can be
queried to obtain **predictions**. [for Ludwig]_"

Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - **Uber**
[(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

" _ **Netflix** is pleased to announce the open-source release of our **crisis
management** orchestration framework: **Dispatch**! [built with **FastAPI**
]_"

Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix**
[(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

" _I’m over the moon excited about **FastAPI**. It’s so fun!_"

Brian Okken - **[Python Bytes](https://pythonbytes.fm/episodes/show/123/time-
to-right-the-py-wrongs?time_in_sec=855) podcast host**
[(ref)](https://twitter.com/brianokken/status/1112220079972728832)

* * *

" _Honestly, what you've built looks super solid and polished. In many ways,
it's what I wanted **Hug** to be - it's really inspiring to see someone build
that._"

Timothy Crosley - **[Hug](https://github.com/hugapi/hug) creator**
[(ref)](https://news.ycombinator.com/item?id=19455465)

* * *

" _If you're looking to learn one **modern framework** for building REST APIs,
check out **FastAPI** [...] It's fast, easy to use and easy to learn [...]_"

" _We've switched over to **FastAPI** for our **APIs** [...] I think you'll
like it [...]_"

Ines Montani - Matthew Honnibal - **[Explosion AI](https://explosion.ai)
founders - [spaCy](https://spacy.io) creators**
[(ref)](https://twitter.com/_inesmontani/status/1144173225322143744) \-
[(ref)](https://twitter.com/honnibal/status/1144031421859655680)

* * *

" _If anyone is looking to build a production Python API, I would highly
recommend **FastAPI**. It is **beautifully designed** , **simple to use** and
**highly scalable** , it has become a **key component** in our API first
development strategy and is driving many automations and services such as our
Virtual TAC Engineer._"

Deon Pillsbury - **Cisco**
[(ref)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-
activity-6963242628536487936-trAp/)

* * *

## **Typer** , the FastAPI of CLIs¶

[![](https://typer.tiangolo.com/img/logo-margin/logo-margin-
vector.svg)](https://typer.tiangolo.com)

If you are building a CLI app to be used in the terminal instead of a web API,
check out [**Typer**](https://typer.tiangolo.com/).

**Typer** is FastAPI's little sibling. And it's intended to be the **FastAPI
of CLIs**. ⌨️ 🚀

## Requirements¶

FastAPI stands on the shoulders of giants:

  * [Starlette](https://www.starlette.io/) for the web parts.
  * [Pydantic](https://docs.pydantic.dev/) for the data parts.

## Installation¶

Create and activate a [virtual
environment](https://fastapi.tiangolo.com/virtual-environments/) and then
install FastAPI:

    
    
    $ pip install "fastapi[standard]"
    
    ---> 100%
    

**Note** : Make sure you put `"fastapi[standard]"` in quotes to ensure it
works in all terminals.

## Example¶

### Create it¶

  * Create a file `main.py` with:

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

Or use `async def`...

If your code uses `async` / `await`, use `async def`:

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    async def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

**Note** :

If you don't know, check the _"In a hurry?"_ section about [`async` and
`await` in the docs](https://fastapi.tiangolo.com/async/#in-a-hurry).

### Run it¶

Run the server with:

    
    
    $ fastapi dev main.py
    
     ╭────────── FastAPI CLI - Development mode ───────────╮
     │                                                     │
     │  Serving at: http://127.0.0.1:8000                  │
     │                                                     │
     │  API docs: http://127.0.0.1:8000/docs               │
     │                                                     │
     │  Running in development mode, for production use:   │
     │                                                     │
     │  fastapi run                                        │
     │                                                     │
     ╰─────────────────────────────────────────────────────╯
    
    INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [2248755] using WatchFiles
    INFO:     Started server process [2248757]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    

About the command `fastapi dev main.py`...

The command `fastapi dev` reads your `main.py` file, detects the **FastAPI**
app in it, and starts a server using [Uvicorn](https://www.uvicorn.org).

By default, `fastapi dev` will start with auto-reload enabled for local
development.

You can read more about it in the [FastAPI CLI
docs](https://fastapi.tiangolo.com/fastapi-cli/).

### Check it¶

Open your browser at <http://127.0.0.1:8000/items/5?q=somequery>.

You will see the JSON response as:

    
    
    {"item_id": 5, "q": "somequery"}
    

You already created an API that:

  * Receives HTTP requests in the _paths_ `/` and `/items/{item_id}`.
  * Both _paths_ take `GET` _operations_ (also known as HTTP _methods_ ).
  * The _path_ `/items/{item_id}` has a _path parameter_ `item_id` that should be an `int`.
  * The _path_ `/items/{item_id}` has an optional `str` _query parameter_ `q`.

### Interactive API docs¶

Now go to <http://127.0.0.1:8000/docs>.

You will see the automatic interactive API documentation (provided by [Swagger
UI](https://github.com/swagger-api/swagger-ui)):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-
simple.png)

### Alternative API docs¶

And now, go to <http://127.0.0.1:8000/redoc>.

You will see the alternative automatic documentation (provided by
[ReDoc](https://github.com/Rebilly/ReDoc)):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## Example upgrade¶

Now modify the file `main.py` to receive a body from a `PUT` request.

Declare the body using standard Python types, thanks to Pydantic.

    
    
    from typing import Union
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        price: float
        is_offer: Union[bool, None] = None
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    
    
    @app.put("/items/{item_id}")
    def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}
    

The `fastapi dev` server should reload automatically.

### Interactive API docs upgrade¶

Now go to <http://127.0.0.1:8000/docs>.

  * The interactive API documentation will be automatically updated, including the new body:

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

  * Click on the button "Try it out", it allows you to fill the parameters and directly interact with the API:

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

  * Then click on the "Execute" button, the user interface will communicate with your API, send the parameters, get the results and show them on the screen:

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### Alternative API docs upgrade¶

And now, go to <http://127.0.0.1:8000/redoc>.

  * The alternative documentation will also reflect the new query parameter and body:

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### Recap¶

In summary, you declare **once** the types of parameters, body, etc. as
function parameters.

You do that with standard modern Python types.

You don't have to learn a new syntax, the methods or classes of a specific
library, etc.

Just standard **Python**.

For example, for an `int`:

    
    
    item_id: int
    

or for a more complex `Item` model:

    
    
    item: Item
    

...and with that single declaration you get:

  * Editor support, including:
    * Completion.
    * Type checks.
  * Validation of data:
    * Automatic and clear errors when the data is invalid.
    * Validation even for deeply nested JSON objects.
  * Conversion of input data: coming from the network to Python data and types. Reading from:
    * JSON.
    * Path parameters.
    * Query parameters.
    * Cookies.
    * Headers.
    * Forms.
    * Files.
  * Conversion of output data: converting from Python data and types to network data (as JSON):
    * Convert Python types (`str`, `int`, `float`, `bool`, `list`, etc).
    * `datetime` objects.
    * `UUID` objects.
    * Database models.
    * ...and many more.
  * Automatic interactive API documentation, including 2 alternative user interfaces:
    * Swagger UI.
    * ReDoc.

* * *

Coming back to the previous code example, **FastAPI** will:

  * Validate that there is an `item_id` in the path for `GET` and `PUT` requests.
  * Validate that the `item_id` is of type `int` for `GET` and `PUT` requests.
    * If it is not, the client will see a useful, clear error.
  * Check if there is an optional query parameter named `q` (as in `http://127.0.0.1:8000/items/foo?q=somequery`) for `GET` requests.
    * As the `q` parameter is declared with `= None`, it is optional.
    * Without the `None` it would be required (as is the body in the case with `PUT`).
  * For `PUT` requests to `/items/{item_id}`, read the body as JSON:
    * Check that it has a required attribute `name` that should be a `str`.
    * Check that it has a required attribute `price` that has to be a `float`.
    * Check that it has an optional attribute `is_offer`, that should be a `bool`, if present.
    * All this would also work for deeply nested JSON objects.
  * Convert from and to JSON automatically.
  * Document everything with OpenAPI, that can be used by:
    * Interactive documentation systems.
    * Automatic client code generation systems, for many languages.
  * Provide 2 interactive documentation web interfaces directly.

* * *

We just scratched the surface, but you already get the idea of how it all
works.

Try changing the line with:

    
    
        return {"item_name": item.name, "item_id": item_id}
    

...from:

    
    
            ... "item_name": item.name ...
    

...to:

    
    
            ... "item_price": item.price ...
    

...and see how your editor will auto-complete the attributes and know their
types:

![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

For a more complete example including more features, see the [Tutorial - User
Guide](https://fastapi.tiangolo.com/tutorial/).

**Spoiler alert** : the tutorial - user guide includes:

  * Declaration of **parameters** from other different places as: **headers** , **cookies** , **form fields** and **files**.
  * How to set **validation constraints** as `maximum_length` or `regex`.
  * A very powerful and easy to use **Dependency Injection** system.
  * Security and authentication, including support for **OAuth2** with **JWT tokens** and **HTTP Basic** auth.
  * More advanced (but equally easy) techniques for declaring **deeply nested JSON models** (thanks to Pydantic).
  * **GraphQL** integration with [Strawberry](https://strawberry.rocks) and other libraries.
  * Many extra features (thanks to Starlette) as:
    * **WebSockets**
    * extremely easy tests based on HTTPX and `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ...and more.

## Performance¶

Independent TechEmpower benchmarks show **FastAPI** applications running under
Uvicorn as [one of the fastest Python frameworks
available](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7),
only below Starlette and Uvicorn themselves (used internally by FastAPI). (*)

To understand more about it, see the section
[Benchmarks](https://fastapi.tiangolo.com/benchmarks/).

## Dependencies¶

FastAPI depends on Pydantic and Starlette.

### `standard` Dependencies¶

When you install FastAPI with `pip install "fastapi[standard]"` it comes with
the `standard` group of optional dependencies:

Used by Pydantic:

  * [`email-validator`](https://github.com/JoshData/python-email-validator) \- for email validation.

Used by Starlette:

  * [`httpx`](https://www.python-httpx.org) \- Required if you want to use the `TestClient`.
  * [`jinja2`](https://jinja.palletsprojects.com) \- Required if you want to use the default template configuration.
  * [`python-multipart`](https://github.com/Kludex/python-multipart) \- Required if you want to support form "parsing", with `request.form()`.

Used by FastAPI / Starlette:

  * [`uvicorn`](https://www.uvicorn.org) \- for the server that loads and serves your application. This includes `uvicorn[standard]`, which includes some dependencies (e.g. `uvloop`) needed for high performance serving.
  * `fastapi-cli` \- to provide the `fastapi` command.

### Without `standard` Dependencies¶

If you don't want to include the `standard` optional dependencies, you can
install with `pip install fastapi` instead of `pip install
"fastapi[standard]"`.

### Additional Optional Dependencies¶

There are some additional dependencies you might want to install.

Additional optional Pydantic dependencies:

  * [`pydantic-settings`](https://docs.pydantic.dev/latest/usage/pydantic_settings/) \- for settings management.
  * [`pydantic-extra-types`](https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/) \- for extra types to be used with Pydantic.

Additional optional FastAPI dependencies:

  * [`orjson`](https://github.com/ijl/orjson) \- Required if you want to use `ORJSONResponse`.
  * [`ujson`](https://github.com/esnme/ultrajson) \- Required if you want to use `UJSONResponse`.

## License¶

This project is licensed under the terms of the MIT license.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!

Back to top

  *[Completion]: also known as auto-complete, autocompletion, IntelliSense
  *[CLI]: Command Line Interface
  *[Conversion]: also known as: serialization, parsing, marshalling
  *[Dependency Injection]: also known as components, resources, providers, services, injectables
  *["parsing"]: converting the string that comes from an HTTP request into Python data



---

# https://fastapi.tiangolo.com/newsletter/



[ ![logo](../img/icon-white.svg) ](.. "FastAPI") FastAPI

[ fastapi/fastapi  ](https://github.com/fastapi/fastapi "Go to repository")

  * [ FastAPI  ](..)
  * [ Features  ](../features/)
  * [ Learn  ](../learn/)

Learn

    * [ Python Types Intro  ](../python-types/)
    * [ Concurrency and async / await  ](../async/)
    * [ Environment Variables  ](../environment-variables/)
    * [ Virtual Environments  ](../virtual-environments/)
    * [ Tutorial - User Guide  ](../tutorial/)

Tutorial - User Guide

      * [ First Steps  ](../tutorial/first-steps/)
      * [ Path Parameters  ](../tutorial/path-params/)
      * [ Query Parameters  ](../tutorial/query-params/)
      * [ Request Body  ](../tutorial/body/)
      * [ Query Parameters and String Validations  ](../tutorial/query-params-str-validations/)
      * [ Path Parameters and Numeric Validations  ](../tutorial/path-params-numeric-validations/)
      * [ Query Parameter Models  ](../tutorial/query-param-models/)
      * [ Body - Multiple Parameters  ](../tutorial/body-multiple-params/)
      * [ Body - Fields  ](../tutorial/body-fields/)
      * [ Body - Nested Models  ](../tutorial/body-nested-models/)
      * [ Declare Request Example Data  ](../tutorial/schema-extra-example/)
      * [ Extra Data Types  ](../tutorial/extra-data-types/)
      * [ Cookie Parameters  ](../tutorial/cookie-params/)
      * [ Header Parameters  ](../tutorial/header-params/)
      * [ Cookie Parameter Models  ](../tutorial/cookie-param-models/)
      * [ Header Parameter Models  ](../tutorial/header-param-models/)
      * [ Response Model - Return Type  ](../tutorial/response-model/)
      * [ Extra Models  ](../tutorial/extra-models/)
      * [ Response Status Code  ](../tutorial/response-status-code/)
      * [ Form Data  ](../tutorial/request-forms/)
      * [ Form Models  ](../tutorial/request-form-models/)
      * [ Request Files  ](../tutorial/request-files/)
      * [ Request Forms and Files  ](../tutorial/request-forms-and-files/)
      * [ Handling Errors  ](../tutorial/handling-errors/)
      * [ Path Operation Configuration  ](../tutorial/path-operation-configuration/)
      * [ JSON Compatible Encoder  ](../tutorial/encoder/)
      * [ Body - Updates  ](../tutorial/body-updates/)
      * [ Dependencies  ](../tutorial/dependencies/)

Dependencies

        * [ Classes as Dependencies  ](../tutorial/dependencies/classes-as-dependencies/)
        * [ Sub-dependencies  ](../tutorial/dependencies/sub-dependencies/)
        * [ Dependencies in path operation decorators  ](../tutorial/dependencies/dependencies-in-path-operation-decorators/)
        * [ Global Dependencies  ](../tutorial/dependencies/global-dependencies/)
        * [ Dependencies with yield  ](../tutorial/dependencies/dependencies-with-yield/)
      * [ Security  ](../tutorial/security/)

Security

        * [ Security - First Steps  ](../tutorial/security/first-steps/)
        * [ Get Current User  ](../tutorial/security/get-current-user/)
        * [ Simple OAuth2 with Password and Bearer  ](../tutorial/security/simple-oauth2/)
        * [ OAuth2 with Password (and hashing), Bearer with JWT tokens  ](../tutorial/security/oauth2-jwt/)
      * [ Middleware  ](../tutorial/middleware/)
      * [ CORS (Cross-Origin Resource Sharing)  ](../tutorial/cors/)
      * [ SQL (Relational) Databases  ](../tutorial/sql-databases/)
      * [ Bigger Applications - Multiple Files  ](../tutorial/bigger-applications/)
      * [ Background Tasks  ](../tutorial/background-tasks/)
      * [ Metadata and Docs URLs  ](../tutorial/metadata/)
      * [ Static Files  ](../tutorial/static-files/)
      * [ Testing  ](../tutorial/testing/)
      * [ Debugging  ](../tutorial/debugging/)
    * [ Advanced User Guide  ](../advanced/)

Advanced User Guide

      * [ Path Operation Advanced Configuration  ](../advanced/path-operation-advanced-configuration/)
      * [ Additional Status Codes  ](../advanced/additional-status-codes/)
      * [ Return a Response Directly  ](../advanced/response-directly/)
      * [ Custom Response - HTML, Stream, File, others  ](../advanced/custom-response/)
      * [ Additional Responses in OpenAPI  ](../advanced/additional-responses/)
      * [ Response Cookies  ](../advanced/response-cookies/)
      * [ Response Headers  ](../advanced/response-headers/)
      * [ Response - Change Status Code  ](../advanced/response-change-status-code/)
      * [ Advanced Dependencies  ](../advanced/advanced-dependencies/)
      * [ Advanced Security  ](../advanced/security/)

Advanced Security

        * [ OAuth2 scopes  ](../advanced/security/oauth2-scopes/)
        * [ HTTP Basic Auth  ](../advanced/security/http-basic-auth/)
      * [ Using the Request Directly  ](../advanced/using-request-directly/)
      * [ Using Dataclasses  ](../advanced/dataclasses/)
      * [ Advanced Middleware  ](../advanced/middleware/)
      * [ Sub Applications - Mounts  ](../advanced/sub-applications/)
      * [ Behind a Proxy  ](../advanced/behind-a-proxy/)
      * [ Templates  ](../advanced/templates/)
      * [ WebSockets  ](../advanced/websockets/)
      * [ Lifespan Events  ](../advanced/events/)
      * [ Testing WebSockets  ](../advanced/testing-websockets/)
      * [ Testing Events: startup - shutdown  ](../advanced/testing-events/)
      * [ Testing Dependencies with Overrides  ](../advanced/testing-dependencies/)
      * [ Async Tests  ](../advanced/async-tests/)
      * [ Settings and Environment Variables  ](../advanced/settings/)
      * [ OpenAPI Callbacks  ](../advanced/openapi-callbacks/)
      * [ OpenAPI Webhooks  ](../advanced/openapi-webhooks/)
      * [ Including WSGI - Flask, Django, others  ](../advanced/wsgi/)
      * [ Generate Clients  ](../advanced/generate-clients/)
    * [ FastAPI CLI  ](../fastapi-cli/)
    * [ Deployment  ](../deployment/)

Deployment

      * [ About FastAPI versions  ](../deployment/versions/)
      * [ About HTTPS  ](../deployment/https/)
      * [ Run a Server Manually  ](../deployment/manually/)
      * [ Deployments Concepts  ](../deployment/concepts/)
      * [ Deploy FastAPI on Cloud Providers  ](../deployment/cloud/)
      * [ Server Workers - Uvicorn with Workers  ](../deployment/server-workers/)
      * [ FastAPI in Containers - Docker  ](../deployment/docker/)
    * [ How To - Recipes  ](../how-to/)

How To - Recipes

      * [ General - How To - Recipes  ](../how-to/general/)
      * [ GraphQL  ](../how-to/graphql/)
      * [ Custom Request and APIRoute class  ](../how-to/custom-request-and-route/)
      * [ Conditional OpenAPI  ](../how-to/conditional-openapi/)
      * [ Extending OpenAPI  ](../how-to/extending-openapi/)
      * [ Separate OpenAPI Schemas for Input and Output or Not  ](../how-to/separate-openapi-schemas/)
      * [ Custom Docs UI Static Assets (Self-Hosting)  ](../how-to/custom-docs-ui-assets/)
      * [ Configure Swagger UI  ](../how-to/configure-swagger-ui/)
      * [ Testing a Database  ](../how-to/testing-database/)
  * [ Reference  ](../reference/)

Reference

    * [ `FastAPI` class  ](../reference/fastapi/)
    * [ Request Parameters  ](../reference/parameters/)
    * [ Status Codes  ](../reference/status/)
    * [ `UploadFile` class  ](../reference/uploadfile/)
    * [ Exceptions - `HTTPException` and `WebSocketException` ](../reference/exceptions/)
    * [ Dependencies - `Depends()` and `Security()` ](../reference/dependencies/)
    * [ `APIRouter` class  ](../reference/apirouter/)
    * [ Background Tasks - `BackgroundTasks` ](../reference/background/)
    * [ `Request` class  ](../reference/request/)
    * [ WebSockets  ](../reference/websockets/)
    * [ `HTTPConnection` class  ](../reference/httpconnection/)
    * [ `Response` class  ](../reference/response/)
    * [ Custom Response Classes - File, HTML, Redirect, Streaming, etc.  ](../reference/responses/)
    * [ Middleware  ](../reference/middleware/)
    * [ OpenAPI  ](../reference/openapi/)

OpenAPI

      * [ OpenAPI `docs` ](../reference/openapi/docs/)
      * [ OpenAPI `models` ](../reference/openapi/models/)
    * [ Security Tools  ](../reference/security/)
    * [ Encoders - `jsonable_encoder` ](../reference/encoders/)
    * [ Static Files - `StaticFiles` ](../reference/staticfiles/)
    * [ Templating - `Jinja2Templates` ](../reference/templating/)
    * [ Test Client - `TestClient` ](../reference/testclient/)
  * [ FastAPI People  ](../fastapi-people/)
  * [ Resources  ](../resources/)

Resources

    * [ Help FastAPI - Get Help  ](../help-fastapi/)
    * [ Development - Contributing  ](../contributing/)
    * [ Full Stack FastAPI Template  ](../project-generation/)
    * [ External Links and Articles  ](../external-links/)
    * [ FastAPI and friends newsletter  ](./)
    * [ Repository Management Tasks  ](../management-tasks/)
  * [ About  ](../about/)

About

    * [ Alternatives, Inspiration and Comparisons  ](../alternatives/)
    * [ History, Design and Future  ](../history-design-future/)
    * [ Benchmarks  ](../benchmarks/)
    * [ Repository Management  ](../management/)
  * [ Release Notes  ](../release-notes/)

  1. [ FastAPI  ](..)
  2. [ Resources  ](../resources/)

# FastAPI and friends newsletter¶

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!

Back to top

  *[Completion]: also known as auto-complete, autocompletion, IntelliSense
  *[CLI]: Command Line Interface
  *[Conversion]: also known as: serialization, parsing, marshalling
  *[Dependency Injection]: also known as components, resources, providers, services, injectables
  *["parsing"]: converting the string that comes from an HTTP request into Python data



---

# https://fastapi.tiangolo.com/az/



[ ![logo](img/icon-white.svg) ](. "FastAPI") FastAPI

[ fastapi/fastapi  ](https://github.com/fastapi/fastapi "Repositoriyaya
baxmaq")

  * FastAPI  [ FastAPI  ](.) Mündəricat 
    * Sponsorlar 
    * Rəylər 
    * **Typer** , CLI-ların FastAPI-ı 
    * Tələblər 
    * Quraşdırma 
    * Nümunə 
      * Kodu yaradaq 
      * Kodu işə salaq 
      * İndi yoxlayaq 
      * İnteraktiv API Sənədləri 
      * Alternativ API sənədləri 
    * Nümunəni Yeniləyək 
      * İnteraktiv API sənədlərindəki dəyişikliyə baxaq 
      * Alternativ API Sənədlərindəki Dəyişikliyə Baxaq 
      * Xülasə 
    * Performans 
    * Məcburi Olmayan Tələblər 
    * Lisenziya 
  * [ Features  ](features/)
  * [ Öyrən  ](learn/)

Öyrən

    * [ Python Types Intro  ](python-types/)
    * [ Concurrency and async / await  ](async/)
    * [ Environment Variables  ](environment-variables/)
    * [ Virtual Environments  ](virtual-environments/)
    * [ Tutorial - User Guide  ](tutorial/)

Tutorial - User Guide

      * [ First Steps  ](tutorial/first-steps/)
      * [ Path Parameters  ](tutorial/path-params/)
      * [ Query Parameters  ](tutorial/query-params/)
      * [ Request Body  ](tutorial/body/)
      * [ Query Parameters and String Validations  ](tutorial/query-params-str-validations/)
      * [ Path Parameters and Numeric Validations  ](tutorial/path-params-numeric-validations/)
      * [ Query Parameter Models  ](tutorial/query-param-models/)
      * [ Body - Multiple Parameters  ](tutorial/body-multiple-params/)
      * [ Body - Fields  ](tutorial/body-fields/)
      * [ Body - Nested Models  ](tutorial/body-nested-models/)
      * [ Declare Request Example Data  ](tutorial/schema-extra-example/)
      * [ Extra Data Types  ](tutorial/extra-data-types/)
      * [ Cookie Parameters  ](tutorial/cookie-params/)
      * [ Header Parameters  ](tutorial/header-params/)
      * [ Cookie Parameter Models  ](tutorial/cookie-param-models/)
      * [ Header Parameter Models  ](tutorial/header-param-models/)
      * [ Response Model - Return Type  ](tutorial/response-model/)
      * [ Extra Models  ](tutorial/extra-models/)
      * [ Response Status Code  ](tutorial/response-status-code/)
      * [ Form Data  ](tutorial/request-forms/)
      * [ Form Models  ](tutorial/request-form-models/)
      * [ Request Files  ](tutorial/request-files/)
      * [ Request Forms and Files  ](tutorial/request-forms-and-files/)
      * [ Handling Errors  ](tutorial/handling-errors/)
      * [ Path Operation Configuration  ](tutorial/path-operation-configuration/)
      * [ JSON Compatible Encoder  ](tutorial/encoder/)
      * [ Body - Updates  ](tutorial/body-updates/)
      * [ Dependencies  ](tutorial/dependencies/)

Dependencies

        * [ Classes as Dependencies  ](tutorial/dependencies/classes-as-dependencies/)
        * [ Sub-dependencies  ](tutorial/dependencies/sub-dependencies/)
        * [ Dependencies in path operation decorators  ](tutorial/dependencies/dependencies-in-path-operation-decorators/)
        * [ Global Dependencies  ](tutorial/dependencies/global-dependencies/)
        * [ Dependencies with yield  ](tutorial/dependencies/dependencies-with-yield/)
      * [ Security  ](tutorial/security/)

Security

        * [ Security - First Steps  ](tutorial/security/first-steps/)
        * [ Get Current User  ](tutorial/security/get-current-user/)
        * [ Simple OAuth2 with Password and Bearer  ](tutorial/security/simple-oauth2/)
        * [ OAuth2 with Password (and hashing), Bearer with JWT tokens  ](tutorial/security/oauth2-jwt/)
      * [ Middleware  ](tutorial/middleware/)
      * [ CORS (Cross-Origin Resource Sharing)  ](tutorial/cors/)
      * [ SQL (Relational) Databases  ](tutorial/sql-databases/)
      * [ Bigger Applications - Multiple Files  ](tutorial/bigger-applications/)
      * [ Background Tasks  ](tutorial/background-tasks/)
      * [ Metadata and Docs URLs  ](tutorial/metadata/)
      * [ Static Files  ](tutorial/static-files/)
      * [ Testing  ](tutorial/testing/)
      * [ Debugging  ](tutorial/debugging/)
    * [ Advanced User Guide  ](advanced/)

Advanced User Guide

      * [ Path Operation Advanced Configuration  ](advanced/path-operation-advanced-configuration/)
      * [ Additional Status Codes  ](advanced/additional-status-codes/)
      * [ Return a Response Directly  ](advanced/response-directly/)
      * [ Custom Response - HTML, Stream, File, others  ](advanced/custom-response/)
      * [ Additional Responses in OpenAPI  ](advanced/additional-responses/)
      * [ Response Cookies  ](advanced/response-cookies/)
      * [ Response Headers  ](advanced/response-headers/)
      * [ Response - Change Status Code  ](advanced/response-change-status-code/)
      * [ Advanced Dependencies  ](advanced/advanced-dependencies/)
      * [ Advanced Security  ](advanced/security/)

Advanced Security

        * [ OAuth2 scopes  ](advanced/security/oauth2-scopes/)
        * [ HTTP Basic Auth  ](advanced/security/http-basic-auth/)
      * [ Using the Request Directly  ](advanced/using-request-directly/)
      * [ Using Dataclasses  ](advanced/dataclasses/)
      * [ Advanced Middleware  ](advanced/middleware/)
      * [ Sub Applications - Mounts  ](advanced/sub-applications/)
      * [ Behind a Proxy  ](advanced/behind-a-proxy/)
      * [ Templates  ](advanced/templates/)
      * [ WebSockets  ](advanced/websockets/)
      * [ Lifespan Events  ](advanced/events/)
      * [ Testing WebSockets  ](advanced/testing-websockets/)
      * [ Testing Events: startup - shutdown  ](advanced/testing-events/)
      * [ Testing Dependencies with Overrides  ](advanced/testing-dependencies/)
      * [ Async Tests  ](advanced/async-tests/)
      * [ Settings and Environment Variables  ](advanced/settings/)
      * [ OpenAPI Callbacks  ](advanced/openapi-callbacks/)
      * [ OpenAPI Webhooks  ](advanced/openapi-webhooks/)
      * [ Including WSGI - Flask, Django, others  ](advanced/wsgi/)
      * [ Generate Clients  ](advanced/generate-clients/)
    * [ FastAPI CLI  ](fastapi-cli/)
    * [ Deployment  ](deployment/)

Deployment

      * [ About FastAPI versions  ](deployment/versions/)
      * [ About HTTPS  ](deployment/https/)
      * [ Run a Server Manually  ](deployment/manually/)
      * [ Deployments Concepts  ](deployment/concepts/)
      * [ Deploy FastAPI on Cloud Providers  ](deployment/cloud/)
      * [ Server Workers - Uvicorn with Workers  ](deployment/server-workers/)
      * [ FastAPI in Containers - Docker  ](deployment/docker/)
    * [ How To - Recipes  ](how-to/)

How To - Recipes

      * [ General - How To - Recipes  ](how-to/general/)
      * [ GraphQL  ](how-to/graphql/)
      * [ Custom Request and APIRoute class  ](how-to/custom-request-and-route/)
      * [ Conditional OpenAPI  ](how-to/conditional-openapi/)
      * [ Extending OpenAPI  ](how-to/extending-openapi/)
      * [ Separate OpenAPI Schemas for Input and Output or Not  ](how-to/separate-openapi-schemas/)
      * [ Custom Docs UI Static Assets (Self-Hosting)  ](how-to/custom-docs-ui-assets/)
      * [ Configure Swagger UI  ](how-to/configure-swagger-ui/)
      * [ Testing a Database  ](how-to/testing-database/)
  * [ Reference  ](reference/)

Reference

    * [ `FastAPI` class  ](reference/fastapi/)
    * [ Request Parameters  ](reference/parameters/)
    * [ Status Codes  ](reference/status/)
    * [ `UploadFile` class  ](reference/uploadfile/)
    * [ Exceptions - `HTTPException` and `WebSocketException` ](reference/exceptions/)
    * [ Dependencies - `Depends()` and `Security()` ](reference/dependencies/)
    * [ `APIRouter` class  ](reference/apirouter/)
    * [ Background Tasks - `BackgroundTasks` ](reference/background/)
    * [ `Request` class  ](reference/request/)
    * [ WebSockets  ](reference/websockets/)
    * [ `HTTPConnection` class  ](reference/httpconnection/)
    * [ `Response` class  ](reference/response/)
    * [ Custom Response Classes - File, HTML, Redirect, Streaming, etc.  ](reference/responses/)
    * [ Middleware  ](reference/middleware/)
    * [ OpenAPI  ](reference/openapi/)

OpenAPI

      * [ OpenAPI `docs` ](reference/openapi/docs/)
      * [ OpenAPI `models` ](reference/openapi/models/)
    * [ Security Tools  ](reference/security/)
    * [ Encoders - `jsonable_encoder` ](reference/encoders/)
    * [ Static Files - `StaticFiles` ](reference/staticfiles/)
    * [ Templating - `Jinja2Templates` ](reference/templating/)
    * [ Test Client - `TestClient` ](reference/testclient/)
  * [ FastAPI People  ](fastapi-people/)
  * [ Resources  ](resources/)

Resources

    * [ Help FastAPI - Get Help  ](help-fastapi/)
    * [ Development - Contributing  ](contributing/)
    * [ Full Stack FastAPI Template  ](project-generation/)
    * [ External Links and Articles  ](external-links/)
    * [ FastAPI and friends newsletter  ](newsletter/)
    * [ Repository Management Tasks  ](management-tasks/)
  * [ About  ](about/)

About

    * [ Alternatives, Inspiration and Comparisons  ](alternatives/)
    * [ History, Design and Future  ](history-design-future/)
    * [ Benchmarks  ](benchmarks/)
    * [ Repository Management  ](management/)
  * [ Release Notes  ](release-notes/)

Mündəricat

  * Sponsorlar 
  * Rəylər 
  * **Typer** , CLI-ların FastAPI-ı 
  * Tələblər 
  * Quraşdırma 
  * Nümunə 
    * Kodu yaradaq 
    * Kodu işə salaq 
    * İndi yoxlayaq 
    * İnteraktiv API Sənədləri 
    * Alternativ API sənədləri 
  * Nümunəni Yeniləyək 
    * İnteraktiv API sənədlərindəki dəyişikliyə baxaq 
    * Alternativ API Sənədlərindəki Dəyişikliyə Baxaq 
    * Xülasə 
  * Performans 
  * Məcburi Olmayan Tələblər 
  * Lisenziya 

# FastAPI

[![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-
teal.png)](https://fastapi.tiangolo.com)

_FastAPI framework, yüksək məshuldarlı, öyrənməsi asan, çevik kodlama,
istifadəyə hazırdır_

[
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master)
](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)
[ ![Əhatə](https://coverage-
badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ](https://coverage-
badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi) [ ![Paket
versiyası](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)
](https://pypi.org/project/fastapi) [ ![Dəstəklənən Python
versiyaları](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
](https://pypi.org/project/fastapi)

* * *

**Sənədlər** : <https://fastapi.tiangolo.com>

**Qaynaq Kodu** : <https://github.com/fastapi/fastapi>

* * *

FastAPI Python ilə API yaratmaq üçün standart Python tip məsləhətlərinə
əsaslanan, müasir, sürətli (yüksək performanslı) framework-dür.

Əsas xüsusiyyətləri bunlardır:

  * **Sürətli** : Çox yüksək performans, **NodeJS** və **Go** səviyyəsində (Starlette və Pydantic-ə təşəkkürlər). Ən sürətli Python frameworklərindən biridir.
  * **Çevik kodlama** : Funksiyanallıqları inkişaf etdirmək sürətini təxminən 200%-dən 300%-ə qədər artırın. *
  * **Daha az xəta** : İnsan (developer) tərəfindən törədilən səhvlərin təxminən 40% -ni azaldın. *
  * **İntuitiv** : Əla redaktor dəstəyi. Hər yerdə otomatik tamamlama. Xətaları müəyyənləşdirməyə daha az vaxt sərf edəcəksiniz.
  * **Asan** : İstifadəsi və öyrənilməsi asan olması üçün nəzərdə tutulmuşdur. Sənədləri oxumaq üçün daha az vaxt ayıracaqsınız.
  * **Qısa** : Kod təkrarlanmasını minimuma endirin. Hər bir parametr tərifində birdən çox xüsusiyyət ilə və daha az səhvlə qarşılaşacaqsınız.
  * **Güclü** : Avtomatik və interaktiv sənədlərlə birlikdə istifadəyə hazır kod əldə edə bilərsiniz.
  * **Standartlara əsaslanan** : API-lar üçün açıq standartlara əsaslanır (və tam uyğun gəlir): [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (əvvəlki adı ilə Swagger) və [JSON Schema](https://json-schema.org/).

* Bu fikirlər daxili development komandasının hazırladıqları məhsulların sınaqlarına əsaslanır.

## Sponsorlar¶

[![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io?ref=fastapi
"BlockBee Cryptocurrency Payment Gateway")
[![](https://fastapi.tiangolo.com/img/sponsors/platform-
sh.png)](https://platform.sh/try-it-now/?utm_source=fastapi-
signup&utm_medium=banner&utm_campaign=FastAPI-signup-June-2023 "Build, run and
scale your apps on a modern, reliable, and secure PaaS.")
[![](https://fastapi.tiangolo.com/img/sponsors/porter.png)](https://www.porter.run
"Deploy FastAPI on AWS with a few clicks")
[![](https://fastapi.tiangolo.com/img/sponsors/bump-
sh.svg)](https://bump.sh/fastapi?utm_source=fastapi&utm_medium=referral&utm_campaign=sponsor
"Automate FastAPI documentation generation with Bump.sh")
[![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-
badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI
files")
[![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge
"Auth, user management and more for your B2B product")
[![](https://fastapi.tiangolo.com/img/sponsors/coherence.png)](https://www.withcoherence.com/?utm_medium=advertising&utm_source=fastapi&utm_campaign=website
"Coherence")
[![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png)](https://www.mongodb.com/developer/languages/python/python-
quickstart-
fastapi/?utm_campaign=fastapi_framework&utm_source=fastapi_sponsorship&utm_medium=web_referral
"Simplify Full Stack Development with FastAPI & MongoDB")
[![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-
gh "Zuplo: Scale, Protect, Document, and Monetize your FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com?utm_source=fastapi
"liblab - Generate SDKs from FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-
fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy
& scale any full-stack web app on Render. Focus on building apps, not infra.")
`[![](https://fastapi.tiangolo.com/img/sponsors/haystack-
fastapi.svg)](https://github.com/deepset-ai/haystack/ "Build powerful search
from composable, open source building blocks")
[![](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/
"Pay as you go for market data")
[![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com?utm_source=fastapi+repo&utm_medium=github+sponsorship
"SDKs for your API | Speakeasy")
[![](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/
"Svix - Webhooks as a service")
[![](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral
"Stainless | Generate best-in-class SDKs")

[Digər sponsorlar](https://fastapi.tiangolo.com/az/fastapi-people/#sponsors)

## Rəylər¶

" _[...] Son günlərdə **FastAPI** -ı çox istifadə edirəm. [...] Əslində onu
komandamın bütün **Microsoftda ML sevislərində** istifadə etməyi planlayıram.
Onların bəziləri **windows** -un əsas məhsuluna və bəzi **Office**
məhsullarına inteqrasiya olunurlar._"

Kabir Khan - **Microsoft** [(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

" _ **FastAPI** kitabxanasını **Proqnozlar** əldə etmək üçün sorğulana bilən
**REST** serverini yaratmaqda istifadə etdik._"

Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - **Uber**
[(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

" _ **Netflix** **böhran idarəçiliyi** orkestrləşmə framework-nün açıq
qaynaqlı buraxılışını elan etməkdən məmnundur: **Dispatch**! [ **FastAPI** ilə
quruldu]_"

Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix**
[(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

" _ **FastAPI** üçün həyəcanlıyam. Çox əyləncəlidir!_"

Brian Okken - **[Python Bytes](https://pythonbytes.fm/episodes/show/123/time-
to-right-the-py-wrongs?time_in_sec=855) podcast host**
[(ref)](https://twitter.com/brianokken/status/1112220079972728832)

* * *

" _Düzünü desəm, sizin qurduğunuz şey həqiqətən möhkəm və peşəkar görünür. Bir
çox cəhətdən **Hug** -un olmasını istədiyim kimdir - kiminsə belə bir şey
qurduğunu görmək həqiqətən ruhlandırıcıdır._"

Timothy Crosley - **[Hug](https://github.com/hugapi/hug) creator**
[(ref)](https://news.ycombinator.com/item?id=19455465)

* * *

" _Əgər REST API-lər yaratmaq üçün **müasir framework** öyrənmək
istəyirsinizsə, **FastAPI** -a baxın [...] Sürətli, istifadəsi və öyrənməsi
asandır. [...]_"

" _ **API** xidmətlərimizi **FastAPI** -a köçürdük [...] Sizin də
bəyənəcəyinizi düşünürük._"

Ines Montani - Matthew Honnibal - **[Explosion AI](https://explosion.ai)
founders - [spaCy](https://spacy.io) creators**
[(ref)](https://twitter.com/_inesmontani/status/1144173225322143744) \-
[(ref)](https://twitter.com/honnibal/status/1144031421859655680)

* * *

" _Python ilə istifadəyə hazır API qurmaq istəyən hər kəsə **FastAPI** -ı
tövsiyə edirəm. **Möhtəşəm şəkildə dizayn edilmiş** , **istifadəsi asan** və
**yüksək dərəcədə genişlənə bilən** -dir, API əsaslı inkişaf strategiyamızın
**əsas komponentinə** çevrilib və Virtual TAC Engineer kimi bir çox
avtomatlaşdırma və servisləri idarə edir._"

Deon Pillsbury - **Cisco**
[(ref)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-
activity-6963242628536487936-trAp/)

* * *

## **Typer** , CLI-ların FastAPI-ı¶

[![](https://typer.tiangolo.com/img/logo-margin/logo-margin-
vector.svg)](https://typer.tiangolo.com)

Əgər siz veb API əvəzinə terminalda istifadə ediləcək CLI proqramı
qurursunuzsa, [**Typer**](https://typer.tiangolo.com/)-a baxa bilərsiniz.

**Typer** FastAPI-ın kiçik qardaşıdır. Və o, CLI-lərin **FastAPI** -ı olmaq
üçün nəzərdə tutulub. ⌨️ 🚀

## Tələblər¶

FastAPI nəhənglərin çiyinlərində dayanır:

  * Web tərəfi üçün [Starlette](https://www.starlette.io/).
  * Data tərəfi üçün [Pydantic](https://docs.pydantic.dev/).

## Quraşdırma¶

    
    
    $ pip install fastapi
    
    ---> 100%
    

Tətbiqimizi əlçatan etmək üçün bizə [Uvicorn](https://www.uvicorn.org) və ya
[Hypercorn](https://github.com/pgjones/hypercorn) kimi ASGI server lazımdır.

    
    
    $ pip install "uvicorn[standard]"
    
    ---> 100%
    

## Nümunə¶

### Kodu yaradaq¶

  * `main.py` adlı fayl yaradaq və ona aşağıdakı kodu yerləşdirək:

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

Və ya `async def`...

Əgər kodunuzda `async` və ya `await` vardırsa `async def` istifadə edə
bilərik:

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    async def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

**Qeyd** :

Əgər bu mövzu haqqında məlumatınız yoxdursa [`async` və `await`
sənədindəki](https://fastapi.tiangolo.com/az/async/#in-a-hurry)
_"Tələsirsən?"_ bölməsinə baxa bilərsiniz.

### Kodu işə salaq¶

Serveri aşağıdakı əmr ilə işə salaq:

    
    
    $ uvicorn main:app --reload
    
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [28720]
    INFO:     Started server process [28722]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    

`uvicorn main:app --reload` əmri haqqında...

`uvicorn main:app` əmri aşağıdakılara instinad edir:

  * `main`: `main.py` faylı (yəni Python "modulu").
  * `app`: `main.py` faylında `app = FastAPI()` sətrində yaratdığımız `FastAPI` obyektidir.
  * `--reload`: kod dəyişikliyindən sonra avtomatik olaraq serveri yenidən işə salır. Bu parametrdən yalnız development mərhələsində istifadə etməliyik.

### İndi yoxlayaq¶

Bu linki brauzerimizdə açaq <http://127.0.0.1:8000/items/5?q=somequery>.

Aşağıdakı kimi bir JSON cavabı görəcəksiniz:

    
    
    {"item_id": 5, "q": "somequery"}
    

Siz artıq bir API yaratmısınız, hansı ki:

  * `/` və `/items/{item_id}` _yollarında_ HTTP sorğularını qəbul edir.
  * Hər iki _yolda_ `GET` _əməliyyatlarını_ (həmçinin HTTP _metodları_ kimi bilinir) aparır.
  * `/items/{item_id}` _yolu_ `item_id` adlı `int` qiyməti almalı olan _yol parametrinə_ sahibdir.
  * `/items/{item_id}` _yolunun_ `q` adlı yol parametri var və bu parametr istəyə bağlı olsa da, `str` qiymətini almalıdır.

### İnteraktiv API Sənədləri¶

İndi <http://127.0.0.1:8000/docs> ünvanına daxil olun.

Avtomatik interaktiv API sənədlərini görəcəksiniz ([Swagger
UI](https://github.com/swagger-api/swagger-ui) tərəfindən təmin edilir):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-
simple.png)

### Alternativ API sənədləri¶

İndi isə <http://127.0.0.1:8000/redoc> ünvanına daxil olun.

[ReDoc](https://github.com/Rebilly/ReDoc) tərəfindən təqdim edilən avtomatik
sənədləri görəcəksiniz:

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## Nümunəni Yeniləyək¶

İndi gəlin `main.py` faylını `PUT` sorğusu ilə birlikdə gövdə qəbul edəcək
şəkildə dəyişdirək.

Pydantic sayəsində standart Python tiplərindən istifadə edərək gövdəni müəyyən
edək.

    
    
    from typing import Union
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        price: float
        is_offer: Union[bool, None] = None
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    
    
    @app.put("/items/{item_id}")
    def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}
    

Server avtomatik olaraq yenidən işə salınmalı idi (çünki biz yuxarıda
`uvicorn` əmri ilə `--reload` parametrindən istifadə etmişik).

### İnteraktiv API sənədlərindəki dəyişikliyə baxaq¶

Yenidən <http://127.0.0.1:8000/docs> ünvanına daxil olun.

  * İnteraktiv API sənədləri yeni gövdə də daxil olmaq ilə avtomatik olaraq yenilənəcək:

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

  * "Try it out" düyməsini klikləyin, bu, parametrləri doldurmağa və API ilə birbaşa əlaqə saxlamağa imkan verir:

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

  * Sonra "Execute" düyməsini klikləyin, istifadəçi interfeysi API ilə əlaqə quracaq, parametrləri göndərəcək, nəticələri əldə edəcək və onları ekranda göstərəcək:

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### Alternativ API Sənədlərindəki Dəyişikliyə Baxaq¶

İndi isə yenidən <http://127.0.0.1:8000/redoc> ünvanına daxil olun.

  * Alternativ sənədlər həm də yeni sorğu parametri və gövdəsini əks etdirəcək:

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### Xülasə¶

Ümumiləşdirsək, parametrlər, gövdə və s. Biz məlumat növlərini **bir dəfə**
funksiya parametrləri kimi təyin edirik.

Bunu standart müasir Python tipləri ilə edirsiniz.

Yeni sintaksis, müəyyən bir kitabxananın metodlarını və ya siniflərini və s.
öyrənmək məcburiyyətində deyilsiniz.

Sadəcə standart **Python**.

Məsələn, `int` üçün:

    
    
    item_id: int
    

və ya daha mürəkkəb `Item` modeli üçün:

    
    
    item: Item
    

...və yalnız parametr tipini təyin etməklə bunları əldə edirsiniz:

  * Redaktor dəstəyi ilə:
    * Avtomatik tamamlama.
    * Tip yoxlanması.
  * Məlumatların Təsdiqlənməsi:
    * Məlumat etibarsız olduqda avtomatik olaraq aydın xətalar göstərir.
    * Hətta çox dərin JSON obyektlərində belə doğrulama aparır.
  * Daxil olan məlumatları çevirmək üçün aşağıdakı məlumat növlərindən istifadə edilir:
    * JSON.
    * Yol parametrləri.
    * Sorğu parametrləri.
    * Çərəzlər.
    * Başlıqlaq.
    * Formalar.
    * Fayllar.
  * Daxil olan məlumatları çevirmək üçün aşağıdakı məlumat növlərindən istifadə edilir (JSON olaraq):
    * Python tiplərinin (`str`, `int`, `float`, `bool`, `list`, və s) çevrilməsi.
    * `datetime` obyektləri.
    * `UUID` obyektləri.
    * Verilənlər bazası modelləri.
    * və daha çoxu...
  * 2 alternativ istifadəçi interfeysi daxil olmaqla avtomatik interaktiv API sənədlərini təmin edir:
    * Swagger UI.
    * ReDoc.

* * *

Gəlin əvvəlki nümunəyə qayıdaq və **FastAPI** -nin nələr edəcəyinə nəzər
salaq:

  * `GET` və `PUT` sorğuları üçün `item_id`-nin yolda olub-olmadığını yoxlayacaq.
  * `item_id`-nin `GET` və `PUT` sorğuları üçün növünün `int` olduğunu yoxlayacaq.
    * Əgər `int` deyilsə, səbəbini göstərən bir xəta mesajı göstərəcəkdir.
  * məcburi olmayan `q` parametrinin `GET` (`http://127.0.0.1:8000/items/foo?q=somequery` burdakı kimi) sorğusu içərisində olub olmadığını yoxlayacaq.
    * `q` parametrini `= None` ilə yaratdığımız üçün, məcburi olmayan parametr olacaq.
    * Əgər `None` olmasaydı, bu məcburi parametr olardı (`PUT` metodunun gövdəsində olduğu kimi).
  * `PUT` sorğusu üçün, `/items/{item_id}` gövdəsini JSON olaraq oxuyacaq:
    * `name` adında məcburi bir parametr olub olmadığını və əgər varsa, tipinin `str` olub olmadığını yoxlayacaq.
    * `price` adında məcburi bir parametr olub olmadığını və əgər varsa, tipinin `float` olub olmadığını yoxlayacaq.
    * `is_offer` adında məcburi olmayan bir parametr olub olmadığını və əgər varsa, tipinin `float` olub olmadığını yoxlayacaq.
    * Bütün bunlar ən dərin JSON obyektlərində belə işləyəcək.
  * Məlumatların JSON-a və JSON-un Python obyektinə çevrilməsi avtomatik həyata keçiriləcək.
  * Hər şeyi OpenAPI ilə uyğun olacaq şəkildə avtomatik olaraq sənədləşdirəcək və onları aşağıdakı kimi istifadə edə biləcək:
    * İnteraktiv sənədləşmə sistemləri.
    * Bir çox proqramlaşdırma dilləri üçün avtomatlaşdırılmış müştəri kodu yaratma sistemləri.
  * 2 interaktiv sənədləşmə veb interfeysini birbaşa təmin edəcək.

* * *

Yeni başlamışıq, amma siz artıq işin məntiqini başa düşmüsünüz.

İndi aşağıdakı sətri dəyişdirməyə çalışın:

    
    
        return {"item_name": item.name, "item_id": item_id}
    

...bundan:

    
    
            ... "item_name": item.name ...
    

...buna:

    
    
            ... "item_price": item.price ...
    

...və redaktorun məlumat tiplərini bildiyini və avtomatik tamaladığını
görəcəksiniz:

![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

Daha çox funksiyaya malik daha dolğun nümunə üçün [Öyrədici - İstifadəçi
Təlimatı](https://fastapi.tiangolo.com/az/tutorial/) səhifəsinə baxa
bilərsiniz.

**Spoiler xəbərdarlığı** : Öyrədici - istifadəçi təlimatına bunlar daxildir:

  * **Parametrlərin** , **başlıqlar** , çərəzlər, **forma sahələri** və **fayllar** olaraq müəyyən edilməsi.
  * `maximum_length` və ya `regex` kimi **doğrulama məhdudiyyətlərinin** necə təyin ediləcəyi.
  * Çox güclü və istifadəsi asan **Dependency Injection** sistemi.
  * Təhlükəsizlik və autentifikasiya, **JWT tokenləri** ilə **OAuth2** dəstəyi və **HTTP Basic** autentifikasiyası.
  * **çox dərin JSON modellərini** müəyyən etmək üçün daha irəli səviyyə (lakin eyni dərəcədə asan) üsullar (Pydantic sayəsində).
  * [Strawberry](https://strawberry.rocks) və digər kitabxanalar ilə **GraphQL** inteqrasiyası.
  * Digər əlavə xüsusiyyətlər (Starlette sayəsində):
    * **WebSockets**
    * HTTPX və `pytest` sayəsində çox asan testlər
    * **CORS**
    * **Cookie Sessions**
    * ...və daha çoxu.

## Performans¶

Müstəqil TechEmpower meyarları göstərir ki, Uvicorn üzərində işləyən
**FastAPI** proqramları [ən sürətli Python kitabxanalarından
biridir](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7),
yalnız Starlette və Uvicorn-un özündən yavaşdır, ki FastAPI bunların üzərinə
qurulmuş bir framework-dür. (*)

Ətraflı məlumat üçün bu bölməyə nəzər salın
[Müqayisələr](https://fastapi.tiangolo.com/az/benchmarks/).

## Məcburi Olmayan Tələblər¶

Pydantic tərəfindən istifadə olunanlar:

  * [`email-validator`](https://github.com/JoshData/python-email-validator) \- e-poçtun yoxlanılması üçün.
  * [`pydantic-settings`](https://docs.pydantic.dev/latest/usage/pydantic_settings/) \- parametrlərin idarə edilməsi üçün.
  * [`pydantic-extra-types`](https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/) \- Pydantic ilə istifadə edilə bilən əlavə tiplər üçün.

Starlette tərəfindən istifadə olunanlar:

  * [`httpx`](https://www.python-httpx.org) \- Əgər `TestClient` strukturundan istifadə edəcəksinizsə, tələb olunur.
  * [`jinja2`](https://jinja.palletsprojects.com) \- Standart şablon konfiqurasiyasından istifadə etmək istəyirsinizsə, tələb olunur.
  * [`python-multipart`](https://github.com/Kludex/python-multipart) \- `request.form()` ilə forma "çevirmə" dəstəyindən istifadə etmək istəyirsinizsə, tələb olunur.
  * [`itsdangerous`](https://pythonhosted.org/itsdangerous/) \- `SessionMiddleware` dəstəyi üçün tələb olunur.
  * [`pyyaml`](https://pyyaml.org/wiki/PyYAMLDocumentation) \- `SchemaGenerator` dəstəyi üçün tələb olunur (Çox güman ki, FastAPI istifadə edərkən buna ehtiyacınız olmayacaq).
  * [`ujson`](https://github.com/esnme/ultrajson) \- `UJSONResponse` istifadə etmək istəyirsinizsə, tələb olunur.

Həm FastAPI, həm də Starlette tərəfindən istifadə olunur:

  * [`uvicorn`](https://www.uvicorn.org) \- Yaratdığımız proqramı servis edəcək veb server kimi fəaliyyət göstərir.
  * [`orjson`](https://github.com/ijl/orjson) \- `ORJSONResponse` istifadə edəcəksinizsə tələb olunur.

Bütün bunları `pip install fastapi[all]` ilə quraşdıra bilərsiniz.

## Lisenziya¶

Bu layihə MIT lisenziyasının şərtlərinə əsasən lisenziyalaşdırılıb.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!

Yuxarıya qayıtmaq

  *[Completion]: also known as auto-complete, autocompletion, IntelliSense
  *[CLI]: Command Line Interface
  *[Conversion]: also known as: serialization, parsing, marshalling
  *[Dependency Injection]: components, resources, providers, services, injectables olaraq da bilinir
  *["parsing"]: converting the string that comes from an HTTP request into Python data
  *[tip məsləhətlərinə]: Tip Məsləhətləri: Type Hints
  *[otomatik tamamlama]: auto-complete, autocompletion, IntelliSense olaraq da bilinir
  *[_yollarında_]: Yol: Path 
  *[gövdə]: Gövdə: Body 
  *[çevirmək]: Çevrilmə: serialization, parsing, marshalling olaraq da bilinir
  *[Yol]: Yol: Path
  *[Sorğu]: Sorğu: Query
  *[Çərəzlər]: Çərəz: Cookie
  *[Başlıqlaq]: Başlıq: Header
  *[Formalar]: Forma: Form
  *[yolda]: Yol: Path
  *[məcburi olmayan]: Məcburi olmayan: Optional
  *[müştəri]: Müştəri: Client
  *[**başlıqlar**]: Başlıq: Header
  *[çərəzlər]: Çərəz: Cookie
  *[Müqayisələr]: Müqayisələr: Benchmarks
  *[şablon]: Şablon: Template
  *["çevirmə"]: HTTP sorğusu ilə alınan string məlumatın Python obyektinə çevrilməsi



---

# https://fastapi.tiangolo.com/bn/



[ ![logo](img/icon-white.svg) ](. "FastAPI") FastAPI

[ fastapi/fastapi  ](https://github.com/fastapi/fastapi "রিপোজিটরিতে যান")

  * FastAPI  [ FastAPI  ](.) সূচি তালিকা 
    * স্পনসর গণ 
    * মতামত সমূহ 
    * **Typer** , CLI এর জন্য FastAPI 
    * প্রয়োজনীয়তা গুলো 
    * ইনস্টলেশন প্রক্রিয়া 
    * উদাহরণ 
      * তৈরি 
      * এটি চালান 
      * এটা চেক করুন 
      * ক্রিয়াশীল API নির্দেশিকা নথি 
      * বিকল্প API নির্দেশিকা নথি 
    * উদাহরণস্বরূপ আপগ্রেড 
      * ক্রিয়াশীল API নির্দেশিকা নথি উন্নীতকরণ 
      * বিকল্প API নির্দেশিকা নথি আপগ্রেড 
      * সংক্ষিপ্তকরণ 
    * কর্মক্ষমতা 
    * ঐচ্ছিক নির্ভরশীলতা 
    * লাইসেন্স 
  * [ Features  ](features/)
  * [ শিখুন  ](learn/)

শিখুন

    * [ পাইথন এর টাইপ্স পরিচিতি  ](python-types/)
    * [ Concurrency and async / await  ](async/)
    * [ Environment Variables  ](environment-variables/)
    * [ Virtual Environments  ](virtual-environments/)
    * [ Tutorial - User Guide  ](tutorial/)

Tutorial - User Guide

      * [ First Steps  ](tutorial/first-steps/)
      * [ Path Parameters  ](tutorial/path-params/)
      * [ Query Parameters  ](tutorial/query-params/)
      * [ Request Body  ](tutorial/body/)
      * [ Query Parameters and String Validations  ](tutorial/query-params-str-validations/)
      * [ Path Parameters and Numeric Validations  ](tutorial/path-params-numeric-validations/)
      * [ Query Parameter Models  ](tutorial/query-param-models/)
      * [ Body - Multiple Parameters  ](tutorial/body-multiple-params/)
      * [ Body - Fields  ](tutorial/body-fields/)
      * [ Body - Nested Models  ](tutorial/body-nested-models/)
      * [ Declare Request Example Data  ](tutorial/schema-extra-example/)
      * [ Extra Data Types  ](tutorial/extra-data-types/)
      * [ Cookie Parameters  ](tutorial/cookie-params/)
      * [ Header Parameters  ](tutorial/header-params/)
      * [ Cookie Parameter Models  ](tutorial/cookie-param-models/)
      * [ Header Parameter Models  ](tutorial/header-param-models/)
      * [ Response Model - Return Type  ](tutorial/response-model/)
      * [ Extra Models  ](tutorial/extra-models/)
      * [ Response Status Code  ](tutorial/response-status-code/)
      * [ Form Data  ](tutorial/request-forms/)
      * [ Form Models  ](tutorial/request-form-models/)
      * [ Request Files  ](tutorial/request-files/)
      * [ Request Forms and Files  ](tutorial/request-forms-and-files/)
      * [ Handling Errors  ](tutorial/handling-errors/)
      * [ Path Operation Configuration  ](tutorial/path-operation-configuration/)
      * [ JSON Compatible Encoder  ](tutorial/encoder/)
      * [ Body - Updates  ](tutorial/body-updates/)
      * [ Dependencies  ](tutorial/dependencies/)

Dependencies

        * [ Classes as Dependencies  ](tutorial/dependencies/classes-as-dependencies/)
        * [ Sub-dependencies  ](tutorial/dependencies/sub-dependencies/)
        * [ Dependencies in path operation decorators  ](tutorial/dependencies/dependencies-in-path-operation-decorators/)
        * [ Global Dependencies  ](tutorial/dependencies/global-dependencies/)
        * [ Dependencies with yield  ](tutorial/dependencies/dependencies-with-yield/)
      * [ Security  ](tutorial/security/)

Security

        * [ Security - First Steps  ](tutorial/security/first-steps/)
        * [ Get Current User  ](tutorial/security/get-current-user/)
        * [ Simple OAuth2 with Password and Bearer  ](tutorial/security/simple-oauth2/)
        * [ OAuth2 with Password (and hashing), Bearer with JWT tokens  ](tutorial/security/oauth2-jwt/)
      * [ Middleware  ](tutorial/middleware/)
      * [ CORS (Cross-Origin Resource Sharing)  ](tutorial/cors/)
      * [ SQL (Relational) Databases  ](tutorial/sql-databases/)
      * [ Bigger Applications - Multiple Files  ](tutorial/bigger-applications/)
      * [ Background Tasks  ](tutorial/background-tasks/)
      * [ Metadata and Docs URLs  ](tutorial/metadata/)
      * [ Static Files  ](tutorial/static-files/)
      * [ Testing  ](tutorial/testing/)
      * [ Debugging  ](tutorial/debugging/)
    * [ Advanced User Guide  ](advanced/)

Advanced User Guide

      * [ Path Operation Advanced Configuration  ](advanced/path-operation-advanced-configuration/)
      * [ Additional Status Codes  ](advanced/additional-status-codes/)
      * [ Return a Response Directly  ](advanced/response-directly/)
      * [ Custom Response - HTML, Stream, File, others  ](advanced/custom-response/)
      * [ Additional Responses in OpenAPI  ](advanced/additional-responses/)
      * [ Response Cookies  ](advanced/response-cookies/)
      * [ Response Headers  ](advanced/response-headers/)
      * [ Response - Change Status Code  ](advanced/response-change-status-code/)
      * [ Advanced Dependencies  ](advanced/advanced-dependencies/)
      * [ Advanced Security  ](advanced/security/)

Advanced Security

        * [ OAuth2 scopes  ](advanced/security/oauth2-scopes/)
        * [ HTTP Basic Auth  ](advanced/security/http-basic-auth/)
      * [ Using the Request Directly  ](advanced/using-request-directly/)
      * [ Using Dataclasses  ](advanced/dataclasses/)
      * [ Advanced Middleware  ](advanced/middleware/)
      * [ Sub Applications - Mounts  ](advanced/sub-applications/)
      * [ Behind a Proxy  ](advanced/behind-a-proxy/)
      * [ Templates  ](advanced/templates/)
      * [ WebSockets  ](advanced/websockets/)
      * [ Lifespan Events  ](advanced/events/)
      * [ Testing WebSockets  ](advanced/testing-websockets/)
      * [ Testing Events: startup - shutdown  ](advanced/testing-events/)
      * [ Testing Dependencies with Overrides  ](advanced/testing-dependencies/)
      * [ Async Tests  ](advanced/async-tests/)
      * [ Settings and Environment Variables  ](advanced/settings/)
      * [ OpenAPI Callbacks  ](advanced/openapi-callbacks/)
      * [ OpenAPI Webhooks  ](advanced/openapi-webhooks/)
      * [ Including WSGI - Flask, Django, others  ](advanced/wsgi/)
      * [ Generate Clients  ](advanced/generate-clients/)
    * [ FastAPI CLI  ](fastapi-cli/)
    * [ Deployment  ](deployment/)

Deployment

      * [ About FastAPI versions  ](deployment/versions/)
      * [ About HTTPS  ](deployment/https/)
      * [ Run a Server Manually  ](deployment/manually/)
      * [ Deployments Concepts  ](deployment/concepts/)
      * [ Deploy FastAPI on Cloud Providers  ](deployment/cloud/)
      * [ Server Workers - Uvicorn with Workers  ](deployment/server-workers/)
      * [ FastAPI in Containers - Docker  ](deployment/docker/)
    * [ How To - Recipes  ](how-to/)

How To - Recipes

      * [ General - How To - Recipes  ](how-to/general/)
      * [ GraphQL  ](how-to/graphql/)
      * [ Custom Request and APIRoute class  ](how-to/custom-request-and-route/)
      * [ Conditional OpenAPI  ](how-to/conditional-openapi/)
      * [ Extending OpenAPI  ](how-to/extending-openapi/)
      * [ Separate OpenAPI Schemas for Input and Output or Not  ](how-to/separate-openapi-schemas/)
      * [ Custom Docs UI Static Assets (Self-Hosting)  ](how-to/custom-docs-ui-assets/)
      * [ Configure Swagger UI  ](how-to/configure-swagger-ui/)
      * [ Testing a Database  ](how-to/testing-database/)
  * [ Reference  ](reference/)

Reference

    * [ `FastAPI` class  ](reference/fastapi/)
    * [ Request Parameters  ](reference/parameters/)
    * [ Status Codes  ](reference/status/)
    * [ `UploadFile` class  ](reference/uploadfile/)
    * [ Exceptions - `HTTPException` and `WebSocketException` ](reference/exceptions/)
    * [ Dependencies - `Depends()` and `Security()` ](reference/dependencies/)
    * [ `APIRouter` class  ](reference/apirouter/)
    * [ Background Tasks - `BackgroundTasks` ](reference/background/)
    * [ `Request` class  ](reference/request/)
    * [ WebSockets  ](reference/websockets/)
    * [ `HTTPConnection` class  ](reference/httpconnection/)
    * [ `Response` class  ](reference/response/)
    * [ Custom Response Classes - File, HTML, Redirect, Streaming, etc.  ](reference/responses/)
    * [ Middleware  ](reference/middleware/)
    * [ OpenAPI  ](reference/openapi/)

OpenAPI

      * [ OpenAPI `docs` ](reference/openapi/docs/)
      * [ OpenAPI `models` ](reference/openapi/models/)
    * [ Security Tools  ](reference/security/)
    * [ Encoders - `jsonable_encoder` ](reference/encoders/)
    * [ Static Files - `StaticFiles` ](reference/staticfiles/)
    * [ Templating - `Jinja2Templates` ](reference/templating/)
    * [ Test Client - `TestClient` ](reference/testclient/)
  * [ FastAPI People  ](fastapi-people/)
  * [ Resources  ](resources/)

Resources

    * [ Help FastAPI - Get Help  ](help-fastapi/)
    * [ Development - Contributing  ](contributing/)
    * [ Full Stack FastAPI Template  ](project-generation/)
    * [ External Links and Articles  ](external-links/)
    * [ FastAPI and friends newsletter  ](newsletter/)
    * [ Repository Management Tasks  ](management-tasks/)
  * [ About  ](about/)

About

    * [ Alternatives, Inspiration and Comparisons  ](alternatives/)
    * [ History, Design and Future  ](history-design-future/)
    * [ Benchmarks  ](benchmarks/)
    * [ Repository Management  ](management/)
  * [ Release Notes  ](release-notes/)

সূচি তালিকা

  * স্পনসর গণ 
  * মতামত সমূহ 
  * **Typer** , CLI এর জন্য FastAPI 
  * প্রয়োজনীয়তা গুলো 
  * ইনস্টলেশন প্রক্রিয়া 
  * উদাহরণ 
    * তৈরি 
    * এটি চালান 
    * এটা চেক করুন 
    * ক্রিয়াশীল API নির্দেশিকা নথি 
    * বিকল্প API নির্দেশিকা নথি 
  * উদাহরণস্বরূপ আপগ্রেড 
    * ক্রিয়াশীল API নির্দেশিকা নথি উন্নীতকরণ 
    * বিকল্প API নির্দেশিকা নথি আপগ্রেড 
    * সংক্ষিপ্তকরণ 
  * কর্মক্ষমতা 
  * ঐচ্ছিক নির্ভরশীলতা 
  * লাইসেন্স 

# FastAPI

[![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-
teal.png)](https://fastapi.tiangolo.com)

_FastAPI উচ্চক্ষমতা সম্পন্ন, সহজে শেখার এবং দ্রুত কোড করে প্রোডাকশনের জন্য
ফ্রামওয়ার্ক।_

[ ![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg)
](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest) [
![Coverage](https://img.shields.io/codecov/c/github/fastapi/fastapi?color=%2334D058)
](https://codecov.io/gh/fastapi/fastapi) [ ![Package
version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)
](https://pypi.org/project/fastapi)

* * *

**নির্দেশিকা নথি** : <https://fastapi.tiangolo.com>

**সোর্স কোড** : <https://github.com/fastapi/fastapi>

* * *

FastAPI একটি আধুনিক, দ্রুত ( বেশি ক্ষমতা ) সম্পন্ন, Python 3.6+ দিয়ে API তৈরির
জন্য স্ট্যান্ডার্ড পাইথন টাইপ ইঙ্গিত ভিত্তিক ওয়েব ফ্রেমওয়ার্ক।

এর মূল বৈশিষ্ট্য গুলো হলঃ

  * **গতি** : এটি **NodeJS** এবং **Go** এর মত কার্যক্ষমতা সম্পন্ন (Starlette এবং Pydantic এর সাহায্যে)। পাইথন এর দ্রুততম ফ্রেমওয়ার্ক গুলোর মধ্যে এটি একটি।
  * **দ্রুত কোড করা** :বৈশিষ্ট্য তৈরির গতি ২০০% থেকে ৩০০% বৃদ্ধি করে৷ *
  * **স্বল্প bugs** : মানুব (ডেভেলপার) সৃষ্ট ত্রুটির প্রায় ৪০% হ্রাস করে। *
  * **স্বজ্ঞাত** : দুর্দান্ত এডিটর সাহায্য Completion নামেও পরিচিত। দ্রুত ডিবাগ করা যায়।

  * **সহজ** : এটি এমন ভাবে সজানো হয়েছে যেন নির্দেশিকা নথি পড়ে সহজে শেখা এবং ব্যবহার করা যায়।

  * **সংক্ষিপ্ত** : কোড পুনরাবৃত্তি কমানোর পাশাপাশি, bug কমায় এবং প্রতিটি প্যারামিটার ঘোষণা থেকে একাধিক ফিচার পাওয়া যায় ।
  * **জোরালো** : স্বয়ংক্রিয় ভাবে তৈরি ক্রিয়াশীল নির্দেশনা নথি (documentation) সহ উৎপাদন উপযোগি (Production-ready) কোড পাওয়া যায়।
  * **মান-ভিত্তিক** : এর ভিত্তি [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (যা পুর্বে Swagger নামে পরিচিত ছিল) এবং [JSON Schema](https://json-schema.org/) এর আদর্শের মানের ওপর

* উৎপাদনমুখি এপ্লিকেশন বানানোর এক দল ডেভেলপার এর মতামত ভিত্তিক ফলাফল।

## স্পনসর গণ¶

[![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io?ref=fastapi
"BlockBee Cryptocurrency Payment Gateway")
[![](https://fastapi.tiangolo.com/img/sponsors/platform-
sh.png)](https://platform.sh/try-it-now/?utm_source=fastapi-
signup&utm_medium=banner&utm_campaign=FastAPI-signup-June-2023 "Build, run and
scale your apps on a modern, reliable, and secure PaaS.")
[![](https://fastapi.tiangolo.com/img/sponsors/porter.png)](https://www.porter.run
"Deploy FastAPI on AWS with a few clicks")
[![](https://fastapi.tiangolo.com/img/sponsors/bump-
sh.svg)](https://bump.sh/fastapi?utm_source=fastapi&utm_medium=referral&utm_campaign=sponsor
"Automate FastAPI documentation generation with Bump.sh")
[![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-
badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI
files")
[![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge
"Auth, user management and more for your B2B product")
[![](https://fastapi.tiangolo.com/img/sponsors/coherence.png)](https://www.withcoherence.com/?utm_medium=advertising&utm_source=fastapi&utm_campaign=website
"Coherence")
[![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png)](https://www.mongodb.com/developer/languages/python/python-
quickstart-
fastapi/?utm_campaign=fastapi_framework&utm_source=fastapi_sponsorship&utm_medium=web_referral
"Simplify Full Stack Development with FastAPI & MongoDB")
[![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-
gh "Zuplo: Scale, Protect, Document, and Monetize your FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com?utm_source=fastapi
"liblab - Generate SDKs from FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-
fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy
& scale any full-stack web app on Render. Focus on building apps, not infra.")
[![](https://fastapi.tiangolo.com/img/sponsors/haystack-
fastapi.svg)](https://github.com/deepset-ai/haystack/ "Build powerful search
from composable, open source building blocks")
[![](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/
"Pay as you go for market data")
[![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com?utm_source=fastapi+repo&utm_medium=github+sponsorship
"SDKs for your API | Speakeasy")
[![](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/
"Svix - Webhooks as a service")
[![](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral
"Stainless | Generate best-in-class SDKs")

[অন্যান্য স্পনসর গণ](https://fastapi.tiangolo.com/fastapi-people/#sponsors)

## মতামত সমূহ¶

" _আমি আজকাল **FastAPI** ব্যবহার করছি। [...] আমরা ভাবছি মাইক্রোসফ্টে **ML
সার্ভিস** এ সকল দলের জন্য এটি ব্যবহার করব। যার মধ্যে কিছু পণ্য **Windows** এ
সংযোযন হয় এবং কিছু **Office** এর সাথে সংযোযন হচ্ছে।_"

কবির খান - **মাইক্রোসফ্টে**
[(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

" _আমরা **FastAPI** লাইব্রেরি গ্রহণ করেছি একটি **REST** সার্ভার তৈরি করতে, যা
**ভবিষ্যদ্বাণী** পাওয়ার জন্য কুয়েরি করা যেতে পারে। [লুডউইগের জন্য]_"

পিয়েরো মোলিনো, ইয়ারোস্লাভ দুদিন, এবং সাই সুমন্থ মিরিয়ালা - **উবার**
[(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

" _ **Netflix** আমাদের **ক্রাইসিস ম্যানেজমেন্ট** অর্কেস্ট্রেশন ফ্রেমওয়ার্ক:
**ডিসপ্যাচ** এর ওপেন সোর্স রিলিজ ঘোষণা করতে পেরে আনন্দিত! [যাকিনা **FastAPI**
দিয়ে নির্মিত]_"

কেভিন গ্লিসন, মার্ক ভিলানোভা, ফরেস্ট মনসেন - **নেটফ্লিক্স**
[(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

" _আমি **FastAPI** নিয়ে চাঁদের সমান উৎসাহিত। এটি খুবই মজার!_"

ব্রায়ান ওকেন - **[পাইথন বাইটস](https://pythonbytes.fm/episodes/show/123/time-
to-right-the-py-wrongs?time_in_sec=855) পডকাস্ট হোস্ট**
[(ref)](https://twitter.com/brianokken/status/1112220079972728832)

* * *

"_সত্যিই, আপনি যা তৈরি করেছেন তা খুব মজবুত এবং পরিপূর্ন৷ অনেক উপায়ে, আমি যা
**Hug** এ করতে চেয়েছিলাম - তা কাউকে তৈরি করতে দেখে আমি সত্যিই অনুপ্রানিত৷_"

টিমোথি ক্রসলে - **[Hug](https://github.com/hugapi/hug) স্রষ্টা**
[(ref)](https://news.ycombinator.com/item?id=19455465)

* * *

"আপনি যদি REST API তৈরির জন্য একটি **আধুনিক ফ্রেমওয়ার্ক** শিখতে চান, তাহলে
**FastAPI** দেখুন [...] এটি দ্রুত, ব্যবহার করা সহজ এবং শিখতেও সহজ [...]_"

" _আমরা আমাদের **APIs** [...] এর জন্য **FastAPI** \- তে এসেছি [...] আমি মনে
করি আপনিও এটি পছন্দ করবেন [...]_"

ইনেস মন্টানি - ম্যাথিউ হোনিবাল - **[Explosion AI](https://explosion.ai)
প্রতিষ্ঠাতা - [spaCy](https://spacy.io) স্রষ্টা**
[(ref)](https://twitter.com/_inesmontani/status/1144173225322143744) \-
[(ref)](https://twitter.com/honnibal/status/1144031421859655680)

* * *

## **Typer** , CLI এর জন্য FastAPI¶

[![](https://typer.tiangolo.com/img/logo-margin/logo-margin-
vector.svg)](https://typer.tiangolo.com)

আপনি যদি CLI অ্যাপ বানাতে চান, যা কিনা ওয়েব API এর পরিবর্তে টার্মিনালে ব্যবহার
হবে, তাহলে দেখুন[ **Typer**](https://typer.tiangolo.com/).

**টাইপার** হল FastAPI এর ছোট ভাইয়ের মত। এবং এটির উদ্দেশ্য ছিল **CLIs এর
FastAPI** হওয়া। ⌨️ 🚀

## প্রয়োজনীয়তা গুলো¶

Python 3.7+

FastAPI কিছু দানবেদের কাঁধে দাঁড়িয়ে আছে:

  * [Starlette](https://www.starlette.io/) ওয়েব অংশের জন্য.
  * [Pydantic](https://docs.pydantic.dev/) ডেটা অংশগুলির জন্য.

## ইনস্টলেশন প্রক্রিয়া¶

    
    
    $ pip install fastapi
    
    ---> 100%
    

আপনার একটি ASGI সার্ভারেরও প্রয়োজন হবে, প্রোডাকশনের জন্য
[Uvicorn](https://www.uvicorn.org) অথবা
[Hypercorn](https://github.com/pgjones/hypercorn).

    
    
    $ pip install "uvicorn[standard]"
    
    ---> 100%
    

## উদাহরণ¶

### তৈরি¶

  * `main.py` নামে একটি ফাইল তৈরি করুন:

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

অথবা ব্যবহার করুন `async def`...

যদি আপনার কোড `async` / `await`, ব্যবহার করে তাহলে `async def` ব্যবহার করুন:

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    async def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

**টীকা** :

আপনি যদি না জানেন, _"তাড়াহুড়ো?"_ বিভাগটি দেখুন [`async` এবং `await` নথির
মধ্যে দেখুন ](https://fastapi.tiangolo.com/async/#in-a-hurry).

### এটি চালান¶

সার্ভার চালু করুন:

    
    
    $ uvicorn main:app --reload
    
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [28720]
    INFO:     Started server process [28722]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    

নির্দেশনা সম্পর্কে `uvicorn main:app --reload`...

`uvicorn main:app` নির্দেশনাটি দ্বারা বোঝায়:

  * `main`: ফাইল `main.py` (পাইথন "মডিউল")।
  * `app`: `app = FastAPI()` লাইন দিয়ে `main.py` এর ভিতরে তৈরি করা অবজেক্ট।
  * `--reload`: কোড পরিবর্তনের পরে সার্ভার পুনরায় চালু করুন। এটি শুধুমাত্র ডেভেলপমেন্ট এর সময় ব্যবহার করুন।

### এটা চেক করুন¶

আপনার ব্রাউজার খুলুন <http://127.0.0.1:8000/items/5?q=somequery> এ।

আপনি JSON রেসপন্স দেখতে পাবেন:

    
    
    {"item_id": 5, "q": "somequery"}
    

আপনি ইতিমধ্যে একটি API তৈরি করেছেন যা:

  * `/` এবং `/items/{item_id}` _paths_ এ HTTP অনুরোধ গ্রহণ করে।
  * উভয় _path_ ই `GET` _অপারেশন_ নেয় ( যা HTTP _methods_ নামেও পরিচিত)।
  * _path_ `/items/{item_id}`-এ একটি _path প্যারামিটার_ `item_id` আছে যা কিনা `int` হতে হবে।
  * _path_ `/items/{item_id}`-এর একটি ঐচ্ছিক `str` _query প্যারামিটার_ `q` আছে।

### ক্রিয়াশীল API নির্দেশিকা নথি¶

এখন যান <http://127.0.0.1:8000/docs>.

আপনি স্বয়ংক্রিয় ভাবে প্রস্তুত ক্রিয়াশীল API নির্দেশিকা নথি দেখতে পাবেন
([Swagger UI](https://github.com/swagger-api/swagger-ui) প্রদত্ত):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-
simple.png)

### বিকল্প API নির্দেশিকা নথি¶

এবং এখন <http://127.0.0.1:8000/redoc> এ যান.

আপনি স্বয়ংক্রিয় ভাবে প্রস্তুত বিকল্প নির্দেশিকা নথি দেখতে পাবেন
([ReDoc](https://github.com/Rebilly/ReDoc) প্রদত্ত):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## উদাহরণস্বরূপ আপগ্রেড¶

এখন `main.py` ফাইলটি পরিবর্তন করুন যেন এটি `PUT` রিকুয়েস্ট থেকে বডি পেতে পারে।

Python স্ট্যান্ডার্ড লাইব্রেরি, Pydantic এর সাহায্যে বডি ঘোষণা করুন।

    
    
    from typing import Union
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        price: float
        is_offer: Union[bool, None] = None
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    
    
    @app.put("/items/{item_id}")
    def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}
    

সার্ভারটি স্বয়ংক্রিয়ভাবে পুনরায় লোড হওয়া উচিত (কারণ আপনি উপরের `uvicorn`
কমান্ডে `--reload` যোগ করেছেন)।

### ক্রিয়াশীল API নির্দেশিকা নথি উন্নীতকরণ¶

এখন <http://127.0.0.1:8000/docs> এডড্রেসে যান.

  * ক্রিয়াশীল API নির্দেশিকা নথিটি স্বয়ংক্রিয়ভাবে উন্নীত হযে যাবে, নতুন বডি সহ:

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

  * "Try it out" বাটনে চাপুন, এটি আপনাকে পেরামিটারগুলো পূরণ করতে এবং API এর সাথে সরাসরি ক্রিয়া-কলাপ করতে দিবে:

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

  * তারপরে "Execute" বাটনে চাপুন, ব্যবহারকারীর ইন্টারফেস আপনার API এর সাথে যোগাযোগ করবে, পেরামিটার পাঠাবে, ফলাফলগুলি পাবে এবং সেগুলি পর্রদায় দেখাবে:

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### বিকল্প API নির্দেশিকা নথি আপগ্রেড¶

এবং এখন <http://127.0.0.1:8000/redoc> এ যান।

  * বিকল্প নির্দেশিকা নথিতেও নতুন কুয়েরি প্যারামিটার এবং বডি প্রতিফলিত হবে:

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### সংক্ষিপ্তকরণ¶

সংক্ষেপে, আপনি **শুধু একবার** প্যারামিটারের ধরন, বডি ইত্যাদি ফাংশন প্যারামিটার
হিসেবে ঘোষণা করেন।

আপনি সেটি আধুনিক পাইথনের সাথে করেন।

আপনাকে নতুন করে নির্দিষ্ট কোন লাইব্রেরির বাক্য গঠন, ফাংশন বা ক্লাস কিছুই শিখতে
হচ্ছে না।

শুধুই আধুনিক **Python 3.6+**

উদাহরণস্বরূপ, `int` এর জন্য:

    
    
    item_id: int
    

অথবা আরও জটিল `Item` মডেলের জন্য:

    
    
    item: Item
    

...এবং সেই একই ঘোষণার সাথে আপনি পাবেন:

  * এডিটর সাহায্য, যেমন
  * সমাপ্তি।
  * ধরণ যাচাই
  * তথ্য যাচাইকরণ:
  * ডেটা অবৈধ হলে স্বয়ংক্রিয় এবং পরিষ্কার ত্রুটির নির্দেশনা।
  * এমনকি গভীরভাবে নেস্ট করা JSON অবজেক্টের জন্য বৈধতা।
  * প্রেরিত তথ্য রূপান্তর: যা নেটওয়ার্ক থেকে পাইথনের তথ্য এবং ধরনে আসে, এবং সেখান থেকে পড়া:

  * JSON।

  * পাথ প্যারামিটার।
  * কুয়েরি প্যারামিটার।
  * কুকিজ
  * হেডার
  * ফর্ম
  * ফাইল

  * আউটপুট ডেটার রূপান্তর: পাইথন ডেটা এবং টাইপ থেকে নেটওয়ার্ক ডেটাতে রূপান্তর করা (JSON হিসাবে): -পাইথন টাইপে রূপান্তর করুন (`str`, `int`, `float`, `bool`, `list`, ইত্যাদি)।

  * `datetime` অবজেক্ট।
  * `UUID` objeঅবজেক্টcts।
  * ডাটাবেস মডেল।
  * ...এবং আরো অনেক।
  * স্বয়ংক্রিয় ক্রিয়াশীল API নির্দেশিকা নথি, 2টি বিকল্প ব্যবহারকারীর ইন্টারফেস সহ:
  * সোয়াগার ইউ আই (Swagger UI)।
  * রিডক (ReDoc)।

* * *

পূর্ববর্তী কোড উদাহরণে ফিরে আসা যাক, **FastAPI** যা করবে:

  * `GET` এবং `PUT` অনুরোধের জন্য পথে `item_id` আছে কিনা তা যাচাই করবে।
  * `GET` এবং `PUT` অনুরোধের জন্য `item_id` টাইপ `int` এর হতে হবে তা যাচাই করবে।
  * যদি না হয় তবে ক্লায়েন্ট একটি উপযুক্ত, পরিষ্কার ত্রুটি দেখতে পাবেন।
  * `GET` অনুরোধের জন্য একটি ঐচ্ছিক ক্যুয়েরি প্যারামিটার নামক `q` (যেমন `http://127.0.0.1:8000/items/foo?q=somequery`) আছে কি তা চেক করবে।
  * যেহেতু `q` প্যারামিটারটি `= None` দিয়ে ঘোষণা করা হয়েছে, তাই এটি ঐচ্ছিক।
  * `None` ছাড়া এটি প্রয়োজনীয় হতো (যেমন `PUT` এর ক্ষেত্রে হয়েছে)।
  * `/items/{item_id}` এর জন্য `PUT` অনুরোধের বডি JSON হিসাবে পড়ুন:
  * লক্ষ করুন, `name` একটি প্রয়োজনীয় অ্যাট্রিবিউট হিসাবে বিবেচনা করেছে এবং এটি `str` হতে হবে।
  * লক্ষ করুন এখানে, `price` অ্যাট্রিবিউটটি আবশ্যক এবং এটি `float` হতে হবে।
  * লক্ষ করুন `is_offer` একটি ঐচ্ছিক অ্যাট্রিবিউট এবং এটি `bool` হতে হবে যদি উপস্থিত থাকে।
  * এই সবটি গভীরভাবে অবস্থানরত JSON অবজেক্টগুলিতেও কাজ করবে।
  * স্বয়ংক্রিয়ভাবে JSON হতে এবং JSON থেকে কনভার্ট করুন।
  * OpenAPI দিয়ে সবকিছু ডকুমেন্ট করুন, যা ব্যবহার করা যেতে পারে:
  * ক্রিয়াশীল নির্দেশিকা নথি।
  * অনেক ভাষার জন্য স্বয়ংক্রিয় ক্লায়েন্ট কোড তৈরির ব্যবস্থা।
  * সরাসরি 2টি ক্রিয়াশীল নির্দেশিকা নথি ওয়েব পৃষ্ঠ প্রদান করা হয়েছে।

* * *

আমরা এতক্ষন শুধু এর পৃষ্ঠ তৈরি করেছি, কিন্তু আপনি ইতমধ্যেই এটি কিভাবে কাজ করে
তার ধারণাও পেয়ে গিয়েছেন।

নিম্নোক্ত লাইন গুলো পরিবর্তন করার চেষ্টা করুন:

    
    
        return {"item_name": item.name, "item_id": item_id}
    

...পুর্বে:

    
    
            ... "item_name": item.name ...
    

...পরবর্তীতে:

    
    
            ... "item_price": item.price ...
    

...এবং দেখুন কিভাবে আপনার এডিটর উপাদানগুলোকে সয়ংক্রিয়ভাবে-সম্পন্ন করবে এবং
তাদের ধরন জানতে পারবে:

![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

আরও বৈশিষ্ট্য সম্পন্ন উদাহরণের জন্য, দেখুন [টিউটোরিয়াল - ব্যবহারকারীর
গাইড](https://fastapi.tiangolo.com/tutorial/).

**স্পয়লার সতর্কতা** : টিউটোরিয়াল - ব্যবহারকারীর গাইড নিম্নোক্ত বিষয়গুলি
অন্তর্ভুক্ত করে:

  * **হেডার** , **কুকিজ** , **ফর্ম ফিল্ড** এবং **ফাইলগুলি** এমন অন্যান্য জায়গা থেকে প্যারামিটার ঘোষণা করা।
  * `maximum_length` বা `regex` এর মতো **যাচাইকরণ বাধামুক্তি** সেট করা হয় কিভাবে, তা নিয়ে আলোচনা করা হবে।
  * একটি খুব শক্তিশালী এবং ব্যবহার করা সহজ ডিপেন্ডেন্সি ইনজেকশন পদ্ধতি
  * **OAuth2** এবং **JWT টোকেন** এবং **HTTP Basic** auth সহ নিরাপত্তা এবং অনুমোদনপ্রাপ্তি সম্পর্কিত বিষয়সমূহের উপর।
  * **গভীরভাবে অবস্থানরত JSON মডেল** ঘোষণা করার জন্য আরও উন্নত (কিন্তু সমান সহজ) কৌশল (Pydantic কে ধন্যবাদ)।
  * আরো অতিরিক্ত বৈশিষ্ট্য (স্টারলেটকে ধন্যবাদ) হিসাবে:
  * **WebSockets**
  * **GraphQL**
  * HTTPX এবং `pytest` ভিত্তিক অত্যন্ত সহজ পরীক্ষা
  * **CORS**
  * **Cookie Sessions**
  * ...এবং আরো।

## কর্মক্ষমতা¶

স্বাধীন TechEmpower Benchmarks দেখায় যে **FastAPI** অ্যাপ্লিকেশনগুলি Uvicorn-
এর অধীনে চলমান দ্রুততম[পাইথন ফ্রেমওয়ার্কগুলির মধ্যে
একটি,](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7)
শুধুমাত্র Starlette এবং Uvicorn-এর পর (FastAPI দ্বারা অভ্যন্তরীণভাবে ব্যবহৃত)।
(*)

এটি সম্পর্কে আরও বুঝতে, দেখুন
[Benchmarks](https://fastapi.tiangolo.com/benchmarks/).

## ঐচ্ছিক নির্ভরশীলতা¶

Pydantic দ্বারা ব্যবহৃত:

  * [`email-validator`](https://github.com/JoshData/python-email-validator) \- ইমেল যাচাইকরণের জন্য।

স্টারলেট দ্বারা ব্যবহৃত:

  * [`httpx`](https://www.python-httpx.org) \- আপনি যদি `TestClient` ব্যবহার করতে চান তাহলে আবশ্যক।
  * [`jinja2`](https://jinja.palletsprojects.com) \- আপনি যদি প্রদত্ত টেমপ্লেট রূপরেখা ব্যবহার করতে চান তাহলে প্রয়োজন।
  * [`python-multipart`](https://github.com/Kludex/python-multipart) \- আপনি যদি ফর্ম সহায়তা করতে চান তাহলে প্রয়োজন "parsing", `request.form()` সহ।
  * [`itsdangerous`](https://pythonhosted.org/itsdangerous/) \- `SessionMiddleware` সহায়তার জন্য প্রয়োজন।
  * [`pyyaml`](https://pyyaml.org/wiki/PyYAMLDocumentation) \- স্টারলেটের SchemaGenerator সাপোর্ট এর জন্য প্রয়োজন (আপনার সম্ভাবত FastAPI প্রয়োজন নেই)।
  * [`graphene`](https://graphene-python.org/) \- `GraphQLApp` সহায়তার জন্য প্রয়োজন।

FastAPI / Starlette দ্বারা ব্যবহৃত:

  * [`uvicorn`](https://www.uvicorn.org) \- সার্ভারের জন্য যা আপনার অ্যাপ্লিকেশন লোড করে এবং পরিবেশন করে।
  * [`orjson`](https://github.com/ijl/orjson) \- আপনি `ORJSONResponse` ব্যবহার করতে চাইলে প্রয়োজন।
  * [`ujson`](https://github.com/esnme/ultrajson) \- আপনি `UJSONResponse` ব্যবহার করতে চাইলে প্রয়োজন।

আপনি এই সব ইনস্টল করতে পারেন `pip install fastapi[all]` দিয়ে.

## লাইসেন্স¶

এই প্রজেক্ট MIT লাইসেন্স নীতিমালার অধীনে শর্তায়িত।

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!

উপরে ফিরে যাও

  *[Completion]: also known as auto-complete, autocompletion, IntelliSense
  *[CLI]: Command Line Interface
  *[Conversion]: also known as: serialization, parsing, marshalling
  *[Dependency Injection]: components, resources, providers, services, injectables olaraq da bilinir
  *["parsing"]: converting the string that comes from an HTTP request into Python data
  *[tip məsləhətlərinə]: Tip Məsləhətləri: Type Hints
  *[otomatik tamamlama]: auto-complete, autocompletion, IntelliSense olaraq da bilinir
  *[_yollarında_]: Yol: Path 
  *[gövdə]: Gövdə: Body 
  *[çevirmək]: Çevrilmə: serialization, parsing, marshalling olaraq da bilinir
  *[Yol]: Yol: Path
  *[Sorğu]: Sorğu: Query
  *[Çərəzlər]: Çərəz: Cookie
  *[Başlıqlaq]: Başlıq: Header
  *[Formalar]: Forma: Form
  *[yolda]: Yol: Path
  *[məcburi olmayan]: Məcburi olmayan: Optional
  *[müştəri]: Müştəri: Client
  *[**başlıqlar**]: Başlıq: Header
  *[çərəzlər]: Çərəz: Cookie
  *[Müqayisələr]: Müqayisələr: Benchmarks
  *[şablon]: Şablon: Template
  *["çevirmə"]: HTTP sorğusu ilə alınan string məlumatın Python obyektinə çevrilməsi
  *[টাইপ্স]: একটি ভেরিয়েবল কি ধরনের ডেটা ধারণ করতে পারে।
  *[রূপান্তর]: যা পরিচিত: serialization, parsing, marshalling
  *[ডিপেন্ডেন্সি ইনজেকশন]: also known as components, resources, providers, services, injectables



---

# https://fastapi.tiangolo.com/de/



[ ![logo](img/icon-white.svg) ](. "FastAPI") FastAPI

[ fastapi/fastapi  ](https://github.com/fastapi/fastapi "Zum Repository")

  * FastAPI  [ FastAPI  ](.) Inhaltsverzeichnis 
    * Sponsoren 
    * Meinungen 
    * **Typer** , das FastAPI der CLIs 
    * Anforderungen 
    * Installation 
    * Beispiel 
      * Erstellung 
      * Starten 
      * Testen 
      * Interaktive API-Dokumentation 
      * Alternative API-Dokumentation 
    * Beispiel Aktualisierung 
      * Aktualisierung der interaktiven API-Dokumentation 
      * Aktualisierung der alternativen API-Dokumentation 
      * Zusammenfassung 
    * Performanz 
    * Optionale Abhängigkeiten 
    * Lizenz 
  * [ Merkmale  ](features/)
  * [ Lernen  ](learn/)

Lernen

    * [ Einführung in Python-Typen  ](python-types/)
    * [ Nebenläufigkeit und async / await  ](async/)
    * [ Environment Variables  ](environment-variables/)
    * [ Virtual Environments  ](virtual-environments/)
    * [ Tutorial – Benutzerhandbuch  ](tutorial/)

Tutorial – Benutzerhandbuch

      * [ Erste Schritte  ](tutorial/first-steps/)
      * [ Pfad-Parameter  ](tutorial/path-params/)
      * [ Query-Parameter  ](tutorial/query-params/)
      * [ Requestbody  ](tutorial/body/)
      * [ Query-Parameter und Stringvalidierung  ](tutorial/query-params-str-validations/)
      * [ Pfad-Parameter und Validierung von Zahlen  ](tutorial/path-params-numeric-validations/)
      * [ Query Parameter Models  ](tutorial/query-param-models/)
      * [ Body – Mehrere Parameter  ](tutorial/body-multiple-params/)
      * [ Body – Felder  ](tutorial/body-fields/)
      * [ Body – Verschachtelte Modelle  ](tutorial/body-nested-models/)
      * [ Beispiel-Request-Daten deklarieren  ](tutorial/schema-extra-example/)
      * [ Zusätzliche Datentypen  ](tutorial/extra-data-types/)
      * [ Cookie-Parameter  ](tutorial/cookie-params/)
      * [ Header-Parameter  ](tutorial/header-params/)
      * [ Cookie Parameter Models  ](tutorial/cookie-param-models/)
      * [ Header Parameter Models  ](tutorial/header-param-models/)
      * [ Responsemodell – Rückgabetyp  ](tutorial/response-model/)
      * [ Extramodelle  ](tutorial/extra-models/)
      * [ Response-Statuscode  ](tutorial/response-status-code/)
      * [ Formulardaten  ](tutorial/request-forms/)
      * [ Form Models  ](tutorial/request-form-models/)
      * [ Dateien im Request  ](tutorial/request-files/)
      * [ Formulardaten und Dateien im Request  ](tutorial/request-forms-and-files/)
      * [ Fehlerbehandlung  ](tutorial/handling-errors/)
      * [ Pfadoperation-Konfiguration  ](tutorial/path-operation-configuration/)
      * [ JSON-kompatibler Encoder  ](tutorial/encoder/)
      * [ Body – Aktualisierungen  ](tutorial/body-updates/)
      * [ Abhängigkeiten  ](tutorial/dependencies/)

Abhängigkeiten

        * [ Klassen als Abhängigkeiten  ](tutorial/dependencies/classes-as-dependencies/)
        * [ Unterabhängigkeiten  ](tutorial/dependencies/sub-dependencies/)
        * [ Abhängigkeiten in Pfadoperation-Dekoratoren  ](tutorial/dependencies/dependencies-in-path-operation-decorators/)
        * [ Globale Abhängigkeiten  ](tutorial/dependencies/global-dependencies/)
        * [ Abhängigkeiten mit yield  ](tutorial/dependencies/dependencies-with-yield/)
      * [ Sicherheit  ](tutorial/security/)

Sicherheit

        * [ Sicherheit – Erste Schritte  ](tutorial/security/first-steps/)
        * [ Aktuellen Benutzer abrufen  ](tutorial/security/get-current-user/)
        * [ Einfaches OAuth2 mit Password und Bearer  ](tutorial/security/simple-oauth2/)
        * [ OAuth2 mit Password (und Hashing), Bearer mit JWT-Tokens  ](tutorial/security/oauth2-jwt/)
      * [ Middleware  ](tutorial/middleware/)
      * [ CORS (Cross-Origin Resource Sharing)  ](tutorial/cors/)
      * [ SQL (Relational) Databases  ](tutorial/sql-databases/)
      * [ Größere Anwendungen – mehrere Dateien  ](tutorial/bigger-applications/)
      * [ Hintergrundtasks  ](tutorial/background-tasks/)
      * [ Metadaten und URLs der Dokumentationen  ](tutorial/metadata/)
      * [ Statische Dateien  ](tutorial/static-files/)
      * [ Testen  ](tutorial/testing/)
      * [ Debugging  ](tutorial/debugging/)
    * [ Handbuch für fortgeschrittene Benutzer  ](advanced/)

Handbuch für fortgeschrittene Benutzer

      * [ Fortgeschrittene Konfiguration der Pfadoperation  ](advanced/path-operation-advanced-configuration/)
      * [ Zusätzliche Statuscodes  ](advanced/additional-status-codes/)
      * [ Eine Response direkt zurückgeben  ](advanced/response-directly/)
      * [ Benutzerdefinierte Response – HTML, Stream, Datei, andere  ](advanced/custom-response/)
      * [ Zusätzliche Responses in OpenAPI  ](advanced/additional-responses/)
      * [ Response-Cookies  ](advanced/response-cookies/)
      * [ Response-Header  ](advanced/response-headers/)
      * [ Response – Statuscode ändern  ](advanced/response-change-status-code/)
      * [ Fortgeschrittene Abhängigkeiten  ](advanced/advanced-dependencies/)
      * [ Fortgeschrittene Sicherheit  ](advanced/security/)

Fortgeschrittene Sicherheit

        * [ OAuth2-Scopes  ](advanced/security/oauth2-scopes/)
        * [ HTTP Basic Auth  ](advanced/security/http-basic-auth/)
      * [ Den Request direkt verwenden  ](advanced/using-request-directly/)
      * [ Verwendung von Datenklassen  ](advanced/dataclasses/)
      * [ Fortgeschrittene Middleware  ](advanced/middleware/)
      * [ Unteranwendungen – Mounts  ](advanced/sub-applications/)
      * [ Hinter einem Proxy  ](advanced/behind-a-proxy/)
      * [ Templates  ](advanced/templates/)
      * [ WebSockets  ](advanced/websockets/)
      * [ Lifespan-Events  ](advanced/events/)
      * [ WebSockets testen  ](advanced/testing-websockets/)
      * [ Events testen: Hochfahren – Herunterfahren  ](advanced/testing-events/)
      * [ Testen mit Ersatz für Abhängigkeiten  ](advanced/testing-dependencies/)
      * [ Asynchrone Tests  ](advanced/async-tests/)
      * [ Einstellungen und Umgebungsvariablen  ](advanced/settings/)
      * [ OpenAPI-Callbacks  ](advanced/openapi-callbacks/)
      * [ OpenAPI-Webhooks  ](advanced/openapi-webhooks/)
      * [ WSGI inkludieren – Flask, Django und andere  ](advanced/wsgi/)
      * [ Clients generieren  ](advanced/generate-clients/)
    * [ FastAPI CLI  ](fastapi-cli/)
    * [ Deployment  ](deployment/)

Deployment

      * [ Über FastAPI-Versionen  ](deployment/versions/)
      * [ Über HTTPS  ](deployment/https/)
      * [ Einen Server manuell ausführen – Uvicorn  ](deployment/manually/)
      * [ Deployment-Konzepte  ](deployment/concepts/)
      * [ FastAPI-Deployment bei Cloud-Anbietern  ](deployment/cloud/)
      * [ Serverworker – Gunicorn mit Uvicorn  ](deployment/server-workers/)
      * [ FastAPI in Containern – Docker  ](deployment/docker/)
    * [ How-To – Rezepte  ](how-to/)

How-To – Rezepte

      * [ Allgemeines – How-To – Rezepte  ](how-to/general/)
      * [ GraphQL  ](how-to/graphql/)
      * [ Benutzerdefinierte Request- und APIRoute-Klasse  ](how-to/custom-request-and-route/)
      * [ Bedingte OpenAPI  ](how-to/conditional-openapi/)
      * [ OpenAPI erweitern  ](how-to/extending-openapi/)
      * [ Separate OpenAPI-Schemas für Eingabe und Ausgabe oder nicht  ](how-to/separate-openapi-schemas/)
      * [ Statische Assets der Dokumentationsoberfläche (selbst hosten)  ](how-to/custom-docs-ui-assets/)
      * [ Swagger-Oberfläche konfigurieren  ](how-to/configure-swagger-ui/)
      * [ Testing a Database  ](how-to/testing-database/)
  * [ Reference  ](reference/)

Reference

    * [ `FastAPI` class  ](reference/fastapi/)
    * [ Request Parameters  ](reference/parameters/)
    * [ Status Codes  ](reference/status/)
    * [ `UploadFile` class  ](reference/uploadfile/)
    * [ Exceptions - `HTTPException` and `WebSocketException` ](reference/exceptions/)
    * [ Dependencies - `Depends()` and `Security()` ](reference/dependencies/)
    * [ `APIRouter` class  ](reference/apirouter/)
    * [ Background Tasks - `BackgroundTasks` ](reference/background/)
    * [ `Request` class  ](reference/request/)
    * [ WebSockets  ](reference/websockets/)
    * [ `HTTPConnection` class  ](reference/httpconnection/)
    * [ `Response` class  ](reference/response/)
    * [ Custom Response Classes - File, HTML, Redirect, Streaming, etc.  ](reference/responses/)
    * [ Middleware  ](reference/middleware/)
    * [ OpenAPI  ](reference/openapi/)

OpenAPI

      * [ OpenAPI `docs` ](reference/openapi/docs/)
      * [ OpenAPI `models` ](reference/openapi/models/)
    * [ Security Tools  ](reference/security/)
    * [ Encoders - `jsonable_encoder` ](reference/encoders/)
    * [ Static Files - `StaticFiles` ](reference/staticfiles/)
    * [ Templating - `Jinja2Templates` ](reference/templating/)
    * [ Test Client - `TestClient` ](reference/testclient/)
  * [ FastAPI People  ](fastapi-people/)
  * [ Ressourcen  ](resources/)

Ressourcen

    * [ FastAPI helfen – Hilfe erhalten  ](help-fastapi/)
    * [ Development - Contributing  ](contributing/)
    * [ Projektgenerierung – Vorlage  ](project-generation/)
    * [ External Links and Articles  ](external-links/)
    * [ FastAPI and friends newsletter  ](newsletter/)
    * [ Repository Management Tasks  ](management-tasks/)
  * [ Über  ](about/)

Über

    * [ Alternativen, Inspiration und Vergleiche  ](alternatives/)
    * [ Geschichte, Design und Zukunft  ](history-design-future/)
    * [ Benchmarks  ](benchmarks/)
    * [ Repository Management  ](management/)
  * [ Release Notes  ](release-notes/)

Inhaltsverzeichnis

  * Sponsoren 
  * Meinungen 
  * **Typer** , das FastAPI der CLIs 
  * Anforderungen 
  * Installation 
  * Beispiel 
    * Erstellung 
    * Starten 
    * Testen 
    * Interaktive API-Dokumentation 
    * Alternative API-Dokumentation 
  * Beispiel Aktualisierung 
    * Aktualisierung der interaktiven API-Dokumentation 
    * Aktualisierung der alternativen API-Dokumentation 
    * Zusammenfassung 
  * Performanz 
  * Optionale Abhängigkeiten 
  * Lizenz 

# FastAPI¶

[![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-
teal.png)](https://fastapi.tiangolo.com)

_FastAPI Framework, hochperformant, leicht zu erlernen, schnell zu
programmieren, einsatzbereit_

[
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master)
](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)
[ ![Coverage](https://coverage-
badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ](https://coverage-
badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi) [ ![Package-
Version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)
](https://pypi.org/project/fastapi) [ ![Unterstützte Python-
Versionen](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
](https://pypi.org/project/fastapi)

* * *

**Dokumentation** : <https://fastapi.tiangolo.com>

**Quellcode** : <https://github.com/fastapi/fastapi>

* * *

FastAPI ist ein modernes, schnelles (hoch performantes) Webframework zur
Erstellung von APIs mit Python auf Basis von Standard-Python-Typhinweisen.

Seine Schlüssel-Merkmale sind:

  * **Schnell** : Sehr hohe Leistung, auf Augenhöhe mit **NodeJS** und **Go** (Dank Starlette und Pydantic). Eines der schnellsten verfügbaren Python-Frameworks.

  * **Schnell zu programmieren** : Erhöhen Sie die Geschwindigkeit bei der Entwicklung von Funktionen um etwa 200 % bis 300 %. *

  * **Weniger Bugs** : Verringern Sie die von Menschen (Entwicklern) verursachten Fehler um etwa 40 %. *
  * **Intuitiv** : Exzellente Editor-Unterstützung. Code-Vervollständigung überall. Weniger Debuggen.
  * **Einfach** : So konzipiert, dass es einfach zu benutzen und zu erlernen ist. Weniger Zeit für das Lesen der Dokumentation.
  * **Kurz** : Minimieren Sie die Verdoppelung von Code. Mehrere Funktionen aus jeder Parameterdeklaration. Weniger Bugs.
  * **Robust** : Erhalten Sie produktionsreifen Code. Mit automatischer, interaktiver Dokumentation.
  * **Standards-basiert** : Basierend auf (und vollständig kompatibel mit) den offenen Standards für APIs: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (früher bekannt als Swagger) und [JSON Schema](https://json-schema.org/).

* Schätzung auf Basis von Tests in einem internen Entwicklungsteam, das Produktionsanwendungen erstellt.

## Sponsoren¶

[![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io?ref=fastapi
"BlockBee Cryptocurrency Payment Gateway")
[![](https://fastapi.tiangolo.com/img/sponsors/platform-
sh.png)](https://platform.sh/try-it-now/?utm_source=fastapi-
signup&utm_medium=banner&utm_campaign=FastAPI-signup-June-2023 "Build, run and
scale your apps on a modern, reliable, and secure PaaS.")
[![](https://fastapi.tiangolo.com/img/sponsors/porter.png)](https://www.porter.run
"Deploy FastAPI on AWS with a few clicks")
[![](https://fastapi.tiangolo.com/img/sponsors/bump-
sh.svg)](https://bump.sh/fastapi?utm_source=fastapi&utm_medium=referral&utm_campaign=sponsor
"Automate FastAPI documentation generation with Bump.sh")
[![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-
badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI
files")
[![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge
"Auth, user management and more for your B2B product")
[![](https://fastapi.tiangolo.com/img/sponsors/coherence.png)](https://www.withcoherence.com/?utm_medium=advertising&utm_source=fastapi&utm_campaign=website
"Coherence")
[![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png)](https://www.mongodb.com/developer/languages/python/python-
quickstart-
fastapi/?utm_campaign=fastapi_framework&utm_source=fastapi_sponsorship&utm_medium=web_referral
"Simplify Full Stack Development with FastAPI & MongoDB")
[![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-
gh "Zuplo: Scale, Protect, Document, and Monetize your FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com?utm_source=fastapi
"liblab - Generate SDKs from FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-
fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy
& scale any full-stack web app on Render. Focus on building apps, not infra.")
[![](https://fastapi.tiangolo.com/img/sponsors/haystack-
fastapi.svg)](https://github.com/deepset-ai/haystack/ "Build powerful search
from composable, open source building blocks")
[![](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/
"Pay as you go for market data")
[![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com?utm_source=fastapi+repo&utm_medium=github+sponsorship
"SDKs for your API | Speakeasy")
[![](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/
"Svix - Webhooks as a service")
[![](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral
"Stainless | Generate best-in-class SDKs")

[Andere Sponsoren](https://fastapi.tiangolo.com/de/fastapi-people/#sponsoren)

## Meinungen¶

„ _[...] Ich verwende **FastAPI** heutzutage sehr oft. [...] Ich habe
tatsächlich vor, es für alle **ML-Dienste meines Teams bei Microsoft** zu
verwenden. Einige davon werden in das Kernprodukt **Windows** und einige
**Office** -Produkte integriert._“

Kabir Khan - **Microsoft** [(Ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

„ _Wir haben die **FastAPI** -Bibliothek genommen, um einen **REST** -Server
zu erstellen, der abgefragt werden kann, um **Vorhersagen** zu erhalten. [für
Ludwig]_“

Piero Molino, Yaroslav Dudin, und Sai Sumanth Miryala - **Uber**
[(Ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

„ _ **Netflix** freut sich, die Open-Source-Veröffentlichung unseres
**Krisenmanagement** -Orchestrierung-Frameworks bekannt zu geben:
**Dispatch**! [erstellt mit **FastAPI** ]_“

Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix**
[(Ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

„ _Ich bin überglücklich mit **FastAPI**. Es macht so viel Spaß!_“

Brian Okken - **Host des[Python
Bytes](https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-
wrongs?time_in_sec=855) Podcast**
[(Ref)](https://twitter.com/brianokken/status/1112220079972728832)

* * *

„ _Ehrlich, was Du gebaut hast, sieht super solide und poliert aus. In
vielerlei Hinsicht ist es so, wie ich **Hug** haben wollte – es ist wirklich
inspirierend, jemanden so etwas bauen zu sehen._“

Timothy Crosley - **Autor von[Hug](https://github.com/hugapi/hug)**
[(Ref)](https://news.ycombinator.com/item?id=19455465)

* * *

„ _Wenn Sie ein **modernes Framework** zum Erstellen von REST-APIs erlernen
möchten, schauen Sie sich **FastAPI** an. [...] Es ist schnell, einfach zu
verwenden und leicht zu erlernen [...]_“

„ _Wir haben zu **FastAPI** für unsere **APIs** gewechselt [...] Ich denke, es
wird Ihnen gefallen [...]_“

Ines Montani - Matthew Honnibal - **Gründer von[Explosion
AI](https://explosion.ai) \- Autoren von [spaCy](https://spacy.io)**
[(Ref)](https://twitter.com/_inesmontani/status/1144173225322143744) \-
[(Ref)](https://twitter.com/honnibal/status/1144031421859655680)

* * *

„ _Falls irgendjemand eine Produktions-Python-API erstellen möchte, kann ich
**FastAPI** wärmstens empfehlen. Es ist **wunderschön konzipiert** , **einfach
zu verwenden** und **hoch skalierbar** ; es ist zu einer
**Schlüsselkomponente** in unserer API-First-Entwicklungsstrategie geworden
und treibt viele Automatisierungen und Dienste an, wie etwa unseren virtuellen
TAC-Ingenieur._“

Deon Pillsbury - **Cisco**
[(Ref)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-
activity-6963242628536487936-trAp/)

* * *

## **Typer** , das FastAPI der CLIs¶

[![](https://typer.tiangolo.com/img/logo-margin/logo-margin-
vector.svg)](https://typer.tiangolo.com)

Wenn Sie eine CLI-Anwendung für das Terminal erstellen, anstelle einer Web-
API, schauen Sie sich [**Typer**](https://typer.tiangolo.com/) an.

**Typer** ist die kleine Schwester von FastAPI. Und es soll das **FastAPI der
CLIs** sein. ⌨️ 🚀

## Anforderungen¶

FastAPI steht auf den Schultern von Giganten:

  * [Starlette](https://www.starlette.io/) für die Webanteile.
  * [Pydantic](https://pydantic-docs.helpmanual.io/) für die Datenanteile.

## Installation¶

    
    
    $ pip install fastapi
    
    ---> 100%
    

Sie benötigen außerdem einen ASGI-Server. Für die Produktumgebung
beispielsweise [Uvicorn](https://www.uvicorn.org) oder
[Hypercorn](https://github.com/pgjones/hypercorn).

    
    
    $ pip install "uvicorn[standard]"
    
    ---> 100%
    

## Beispiel¶

### Erstellung¶

  * Erstellen Sie eine Datei `main.py` mit:

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

Oder verwenden Sie `async def` ...

Wenn Ihr Code `async` / `await` verwendet, benutzen Sie `async def`:

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    async def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

**Anmerkung** :

Wenn Sie das nicht kennen, schauen Sie sich den Abschnitt _„In Eile?“_ über
[`async` und `await` in der
Dokumentation](https://fastapi.tiangolo.com/de/async/#in-eile) an.

### Starten¶

Führen Sie den Server aus:

    
    
    $ uvicorn main:app --reload
    
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [28720]
    INFO:     Started server process [28722]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    

Was macht der Befehl `uvicorn main:app --reload` ...

Der Befehl `uvicorn main:app` bezieht sich auf:

  * `main`: die Datei `main.py` (das Python-„Modul“).
  * `app`: das Objekt, das innerhalb von `main.py` mit der Zeile `app = FastAPI()` erzeugt wurde.
  * `--reload`: lässt den Server nach Codeänderungen neu starten. Tun Sie das nur während der Entwicklung.

### Testen¶

Öffnen Sie Ihren Browser unter <http://127.0.0.1:8000/items/5?q=somequery>.

Sie erhalten die JSON-Response:

    
    
    {"item_id": 5, "q": "somequery"}
    

Damit haben Sie bereits eine API erstellt, welche:

  * HTTP-Anfragen auf den _Pfaden_ `/` und `/items/{item_id}` entgegennimmt.
  * Beide _Pfade_ erhalten `GET` _Operationen_ (auch bekannt als HTTP _Methoden_ ).
  * Der _Pfad_ `/items/{item_id}` hat einen _Pfadparameter_ `item_id`, der ein `int` sein sollte.
  * Der _Pfad_ `/items/{item_id}` hat einen optionalen `str` _Query Parameter_ `q`.

### Interaktive API-Dokumentation¶

Gehen Sie nun auf <http://127.0.0.1:8000/docs>.

Sie sehen die automatische interaktive API-Dokumentation (bereitgestellt von
[Swagger UI](https://github.com/swagger-api/swagger-ui)):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-
simple.png)

### Alternative API-Dokumentation¶

Gehen Sie jetzt auf <http://127.0.0.1:8000/redoc>.

Sie sehen die alternative automatische Dokumentation (bereitgestellt von
[ReDoc](https://github.com/Rebilly/ReDoc)):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## Beispiel Aktualisierung¶

Ändern Sie jetzt die Datei `main.py`, um den Body einer `PUT`-Anfrage zu
empfangen.

Deklarieren Sie den Body mithilfe von Standard-Python-Typen, dank Pydantic.

    
    
    from typing import Union
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        price: float
        is_offer: Union[bool, None] = None
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    
    
    @app.put("/items/{item_id}")
    def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}
    

Der Server sollte automatisch neu geladen werden (weil Sie oben `--reload` zum
Befehl `uvicorn` hinzugefügt haben).

### Aktualisierung der interaktiven API-Dokumentation¶

Gehen Sie jetzt auf <http://127.0.0.1:8000/docs>.

  * Die interaktive API-Dokumentation wird automatisch aktualisiert, einschließlich des neuen Bodys:

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

  * Klicken Sie auf die Taste „Try it out“, damit können Sie die Parameter ausfüllen und direkt mit der API interagieren:

![Swagger UI
Interaktion](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

  * Klicken Sie dann auf die Taste „Execute“, die Benutzeroberfläche wird mit Ihrer API kommunizieren, sendet die Parameter, holt die Ergebnisse und zeigt sie auf dem Bildschirm an:

![Swagger UI
Interaktion](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### Aktualisierung der alternativen API-Dokumentation¶

Und nun gehen Sie auf <http://127.0.0.1:8000/redoc>.

  * Die alternative Dokumentation wird ebenfalls den neuen Abfrageparameter und -inhalt widerspiegeln:

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### Zusammenfassung¶

Zusammengefasst deklarieren Sie **einmal** die Typen von Parametern, Body,
etc. als Funktionsparameter.

Das machen Sie mit modernen Standard-Python-Typen.

Sie müssen keine neue Syntax, Methoden oder Klassen einer bestimmten
Bibliothek usw. lernen.

Nur Standard- **Python+**.

Zum Beispiel für ein `int`:

    
    
    item_id: int
    

oder für ein komplexeres `Item`-Modell:

    
    
    item: Item
    

... und mit dieser einen Deklaration erhalten Sie:

  * Editor-Unterstützung, einschließlich:
    * Code-Vervollständigung.
    * Typprüfungen.
  * Validierung von Daten:
    * Automatische und eindeutige Fehler, wenn die Daten ungültig sind.
    * Validierung auch für tief verschachtelte JSON-Objekte.
  * Konvertierung von Eingabedaten: Aus dem Netzwerk kommend, zu Python-Daten und -Typen. Lesen von:
    * JSON.
    * Pfad-Parametern.
    * Abfrage-Parametern.
    * Cookies.
    * Header-Feldern.
    * Formularen.
    * Dateien.
  * Konvertierung von Ausgabedaten: Konvertierung von Python-Daten und -Typen zu Netzwerkdaten (als JSON):
    * Konvertieren von Python-Typen (`str`, `int`, `float`, `bool`, `list`, usw.).
    * `Datetime`-Objekte.
    * `UUID`-Objekte.
    * Datenbankmodelle.
    * ... und viele mehr.
  * Automatische interaktive API-Dokumentation, einschließlich 2 alternativer Benutzeroberflächen:
    * Swagger UI.
    * ReDoc.

* * *

Um auf das vorherige Codebeispiel zurückzukommen, **FastAPI** wird:

  * Überprüfen, dass es eine `item_id` im Pfad für `GET`\- und `PUT`-Anfragen gibt.
  * Überprüfen, ob die `item_id` vom Typ `int` für `GET`\- und `PUT`-Anfragen ist.
    * Falls nicht, wird dem Client ein nützlicher, eindeutiger Fehler angezeigt.
  * Prüfen, ob es einen optionalen Abfrageparameter namens `q` (wie in `http://127.0.0.1:8000/items/foo?q=somequery`) für `GET`-Anfragen gibt.
    * Da der `q`-Parameter mit `= None` deklariert ist, ist er optional.
    * Ohne das `None` wäre er erforderlich (wie der Body im Fall von `PUT`).
  * Bei `PUT`-Anfragen an `/items/{item_id}` den Body als JSON lesen:
    * Prüfen, ob er ein erforderliches Attribut `name` hat, das ein `str` sein muss.
    * Prüfen, ob er ein erforderliches Attribut `price` hat, das ein `float` sein muss.
    * Prüfen, ob er ein optionales Attribut `is_offer` hat, das ein `bool` sein muss, falls vorhanden.
    * All dies würde auch für tief verschachtelte JSON-Objekte funktionieren.
  * Automatisch von und nach JSON konvertieren.
  * Alles mit OpenAPI dokumentieren, welches verwendet werden kann von:
    * Interaktiven Dokumentationssystemen.
    * Automatisch Client-Code generierenden Systemen für viele Sprachen.
  * Zwei interaktive Dokumentation-Webschnittstellen direkt zur Verfügung stellen.

* * *

Wir haben nur an der Oberfläche gekratzt, aber Sie bekommen schon eine
Vorstellung davon, wie das Ganze funktioniert.

Versuchen Sie, diese Zeile zu ändern:

    
    
        return {"item_name": item.name, "item_id": item_id}
    

... von:

    
    
            ... "item_name": item.name ...
    

... zu:

    
    
            ... "item_price": item.price ...
    

... und sehen Sie, wie Ihr Editor die Attribute automatisch ausfüllt und ihre
Typen kennt:

![Editor Unterstützung](https://fastapi.tiangolo.com/img/vscode-
completion.png)

Für ein vollständigeres Beispiel, mit weiteren Funktionen, siehe das [Tutorial
- Benutzerhandbuch](https://fastapi.tiangolo.com/tutorial/).

**Spoiler-Alarm** : Das Tutorial - Benutzerhandbuch enthält:

  * Deklaration von **Parametern** von anderen verschiedenen Stellen wie: **Header-Felder** , **Cookies** , **Formularfelder** und **Dateien**.
  * Wie man **Validierungseinschränkungen** wie `maximum_length` oder `regex` setzt.
  * Ein sehr leistungsfähiges und einfach zu bedienendes System für **Dependency Injection**.
  * Sicherheit und Authentifizierung, einschließlich Unterstützung für **OAuth2** mit **JWT-Tokens** und **HTTP-Basic** -Authentifizierung.
  * Fortgeschrittenere (aber ebenso einfache) Techniken zur Deklaration **tief verschachtelter JSON-Modelle** (dank Pydantic).
  * **GraphQL** Integration mit [Strawberry](https://strawberry.rocks) und anderen Bibliotheken.
  * Viele zusätzliche Funktionen (dank Starlette) wie:
    * **WebSockets**
    * extrem einfache Tests auf Basis von `httpx` und `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ... und mehr.

## Performanz¶

Unabhängige TechEmpower-Benchmarks zeigen **FastAPI** -Anwendungen, die unter
Uvicorn laufen, als [eines der schnellsten verfügbaren Python-
Frameworks](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7),
nur noch hinter Starlette und Uvicorn selbst (intern von FastAPI verwendet).

Um mehr darüber zu erfahren, siehe den Abschnitt
[Benchmarks](https://fastapi.tiangolo.com/benchmarks/).

## Optionale Abhängigkeiten¶

Wird von Pydantic verwendet:

  * [`email-validator`](https://github.com/JoshData/python-email-validator) \- für E-Mail-Validierung.
  * [`pydantic-settings`](https://docs.pydantic.dev/latest/usage/pydantic_settings/) \- für die Verwaltung von Einstellungen.
  * [`pydantic-extra-types`](https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/) \- für zusätzliche Typen, mit Pydantic zu verwenden.

Wird von Starlette verwendet:

  * [`httpx`](https://www.python-httpx.org) \- erforderlich, wenn Sie den `TestClient` verwenden möchten.
  * [`jinja2`](https://jinja.palletsprojects.com) \- erforderlich, wenn Sie die Standardkonfiguration für Templates verwenden möchten.
  * [`python-multipart`](https://github.com/Kludex/python-multipart) \- erforderlich, wenn Sie Formulare mittels `request.form()` „parsen“ möchten.
  * [`itsdangerous`](https://pythonhosted.org/itsdangerous/) \- erforderlich für `SessionMiddleware` Unterstützung.
  * [`pyyaml`](https://pyyaml.org/wiki/PyYAMLDocumentation) \- erforderlich für Starlette's `SchemaGenerator` Unterstützung (Sie brauchen das wahrscheinlich nicht mit FastAPI).
  * [`ujson`](https://github.com/esnme/ultrajson) \- erforderlich, wenn Sie `UJSONResponse` verwenden möchten.

Wird von FastAPI / Starlette verwendet:

  * [`uvicorn`](https://www.uvicorn.org) \- für den Server, der Ihre Anwendung lädt und serviert.
  * [`orjson`](https://github.com/ijl/orjson) \- erforderlich, wenn Sie `ORJSONResponse` verwenden möchten.

Sie können diese alle mit `pip install "fastapi[all]"` installieren.

## Lizenz¶

Dieses Projekt ist unter den Bedingungen der MIT-Lizenz lizenziert.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!

Zurück zum Seitenanfang

  *[Completion]: also known as auto-complete, autocompletion, IntelliSense
  *[CLI]: Command Line Interface – Kommandozeilen-Schnittstelle
  *[Conversion]: also known as: serialization, parsing, marshalling
  *[Dependency Injection]: Dependency Injection – Einbringen von Abhängigkeiten: Auch bekannt als Komponenten, Ressourcen, Provider, Services, Injectables
  *["parsing"]: converting the string that comes from an HTTP request into Python data
  *[tip məsləhətlərinə]: Tip Məsləhətləri: Type Hints
  *[otomatik tamamlama]: auto-complete, autocompletion, IntelliSense olaraq da bilinir
  *[_yollarında_]: Yol: Path 
  *[gövdə]: Gövdə: Body 
  *[çevirmək]: Çevrilmə: serialization, parsing, marshalling olaraq da bilinir
  *[Yol]: Yol: Path
  *[Sorğu]: Sorğu: Query
  *[Çərəzlər]: Çərəz: Cookie
  *[Başlıqlaq]: Başlıq: Header
  *[Formalar]: Forma: Form
  *[yolda]: Yol: Path
  *[məcburi olmayan]: Məcburi olmayan: Optional
  *[müştəri]: Müştəri: Client
  *[**başlıqlar**]: Başlıq: Header
  *[çərəzlər]: Çərəz: Cookie
  *[Müqayisələr]: Müqayisələr: Benchmarks
  *[şablon]: Şablon: Template
  *["çevirmə"]: HTTP sorğusu ilə alınan string məlumatın Python obyektinə çevrilməsi
  *[টাইপ্স]: একটি ভেরিয়েবল কি ধরনের ডেটা ধারণ করতে পারে।
  *[রূপান্তর]: যা পরিচিত: serialization, parsing, marshalling
  *[ডিপেন্ডেন্সি ইনজেকশন]: also known as components, resources, providers, services, injectables
  *[Code-Vervollständigung]: auch bekannt als Autovervollständigung, Autocompletion, IntelliSense
  *[ASGI]: Asynchronous Server Gateway Interface – Asynchrone Server-Verbindungsschnittstelle
  *[Body]: Body – Körper, Inhalt: Der eigentliche Inhalt einer Nachricht, nicht die Metadaten
  *[Konvertierung]: auch bekannt als: Serialisierung, Parsen, Marshalling
  *[„parsen“]: Konvertieren des Strings, der aus einer HTTP-Anfrage stammt, nach Python-Daten



---

# https://fastapi.tiangolo.com/es/



[ ![logo](img/icon-white.svg) ](. "FastAPI") FastAPI

[ fastapi/fastapi  ](https://github.com/fastapi/fastapi "Ir al repositorio")

  * FastAPI  [ FastAPI  ](.) Tabla de contenidos 
    * Sponsors 
    * Opiniones 
    * **Typer** , el FastAPI de las CLIs 
    * Requisitos 
    * Instalación 
    * Ejemplo 
      * Créalo 
      * Córrelo 
      * Revísalo 
      * Documentación interactiva de la API 
      * Documentación de API Alternativa 
    * Actualización del Ejemplo 
      * Actualización de la Documentación Interactiva de la API 
      * Actualización de la Documentación Alternativa de la API 
      * Resumen 
    * Rendimiento 
    * Dependencias 
      * Dependencias `standard`
      * Sin Dependencias `standard`
      * Dependencias Opcionales Adicionales 
    * Licencia 
  * [ Funcionalidades  ](features/)
  * [ Aprende  ](learn/)

Aprende

    * [ Introducción a Tipos en Python  ](python-types/)
    * [ Concurrencia y async / await  ](async/)
    * [ Variables de Entorno  ](environment-variables/)
    * [ Entornos Virtuales  ](virtual-environments/)
    * [ Tutorial - Guía del Usuario  ](tutorial/)

Tutorial - Guía del Usuario

      * [ Primeros Pasos  ](tutorial/first-steps/)
      * [ Parámetros de Path  ](tutorial/path-params/)
      * [ Parámetros de Query  ](tutorial/query-params/)
      * [ Request Body  ](tutorial/body/)
      * [ Parámetros de Query y Validaciones de String  ](tutorial/query-params-str-validations/)
      * [ Parámetros de Path y Validaciones Numéricas  ](tutorial/path-params-numeric-validations/)
      * [ Modelos de Parámetros Query  ](tutorial/query-param-models/)
      * [ Cuerpo - Múltiples Parámetros  ](tutorial/body-multiple-params/)
      * [ Body - Campos  ](tutorial/body-fields/)
      * [ Cuerpo - Modelos Anidados  ](tutorial/body-nested-models/)
      * [ Declarar Ejemplos de Request  ](tutorial/schema-extra-example/)
      * [ Tipos de Datos Extra  ](tutorial/extra-data-types/)
      * [ Parámetros de Cookie  ](tutorial/cookie-params/)
      * [ Parámetros de Header  ](tutorial/header-params/)
      * [ Modelos de Cookies  ](tutorial/cookie-param-models/)
      * [ Modelos de Parámetros de Header  ](tutorial/header-param-models/)
      * [ Modelo de Response - Tipo de Retorno  ](tutorial/response-model/)
      * [ Modelos Extra  ](tutorial/extra-models/)
      * [ Código de Estado del Response  ](tutorial/response-status-code/)
      * [ Form Data  ](tutorial/request-forms/)
      * [ Modelos de Formulario  ](tutorial/request-form-models/)
      * [ Archivos de Request  ](tutorial/request-files/)
      * [ Request Forms and Files  ](tutorial/request-forms-and-files/)
      * [ Manejo de Errores  ](tutorial/handling-errors/)
      * [ Configuración de Path Operation  ](tutorial/path-operation-configuration/)
      * [ JSON Compatible Encoder  ](tutorial/encoder/)
      * [ Cuerpo - Actualizaciones  ](tutorial/body-updates/)
      * [ Dependencias  ](tutorial/dependencies/)

Dependencias

        * [ Clases como dependencias  ](tutorial/dependencies/classes-as-dependencies/)
        * [ Sub-dependencias  ](tutorial/dependencies/sub-dependencies/)
        * [ Dependencias en decoradores de _path operation_ ](tutorial/dependencies/dependencies-in-path-operation-decorators/)
        * [ Dependencias Globales  ](tutorial/dependencies/global-dependencies/)
        * [ Dependencias con yield  ](tutorial/dependencies/dependencies-with-yield/)
      * [ Seguridad  ](tutorial/security/)

Seguridad

        * [ Seguridad - Primeros pasos  ](tutorial/security/first-steps/)
        * [ Obtener Usuario Actual  ](tutorial/security/get-current-user/)
        * [ Simple OAuth2 con Password y Bearer  ](tutorial/security/simple-oauth2/)
        * [ OAuth2 con Password (y hashing), Bearer con tokens JWT  ](tutorial/security/oauth2-jwt/)
      * [ Middleware  ](tutorial/middleware/)
      * [ CORS (Cross-Origin Resource Sharing)  ](tutorial/cors/)
      * [ Bases de Datos SQL (Relacionales)  ](tutorial/sql-databases/)
      * [ Aplicaciones más grandes - Múltiples archivos  ](tutorial/bigger-applications/)
      * [ Tareas en Segundo Plano  ](tutorial/background-tasks/)
      * [ Metadata y URLs de Docs  ](tutorial/metadata/)
      * [ Archivos Estáticos  ](tutorial/static-files/)
      * [ Testing  ](tutorial/testing/)
      * [ Depuración  ](tutorial/debugging/)
    * [ Guía avanzada del usuario  ](advanced/)

Guía avanzada del usuario

      * [ Configuración Avanzada de Path Operation  ](advanced/path-operation-advanced-configuration/)
      * [ Códigos de Estado Adicionales  ](advanced/additional-status-codes/)
      * [ Devolver una Response Directamente  ](advanced/response-directly/)
      * [ Response Personalizado - HTML, Stream, Archivo, otros  ](advanced/custom-response/)
      * [ Responses Adicionales en OpenAPI  ](advanced/additional-responses/)
      * [ Cookies de Response  ](advanced/response-cookies/)
      * [ Response Headers  ](advanced/response-headers/)
      * [ Response - Cambiar Código de Estado  ](advanced/response-change-status-code/)
      * [ Dependencias Avanzadas  ](advanced/advanced-dependencies/)
      * [ Seguridad Avanzada  ](advanced/security/)

Seguridad Avanzada

        * [ Scopes de OAuth2  ](advanced/security/oauth2-scopes/)
        * [ HTTP Basic Auth  ](advanced/security/http-basic-auth/)
      * [ Usar el Request Directamente  ](advanced/using-request-directly/)
      * [ Usando Dataclasses  ](advanced/dataclasses/)
      * [ Middleware Avanzado  ](advanced/middleware/)
      * [ Sub Aplicaciones - Mounts  ](advanced/sub-applications/)
      * [ Detrás de un Proxy  ](advanced/behind-a-proxy/)
      * [ Plantillas  ](advanced/templates/)
      * [ WebSockets  ](advanced/websockets/)
      * [ Eventos de Lifespan  ](advanced/events/)
      * [ Probando WebSockets  ](advanced/testing-websockets/)
      * [ Testing Events: startup - shutdown  ](advanced/testing-events/)
      * [ Probando Dependencias con Overrides  ](advanced/testing-dependencies/)
      * [ Tests Asíncronos  ](advanced/async-tests/)
      * [ Configuraciones y Variables de Entorno  ](advanced/settings/)
      * [ OpenAPI Callbacks  ](advanced/openapi-callbacks/)
      * [ Webhooks de OpenAPI  ](advanced/openapi-webhooks/)
      * [ Incluyendo WSGI - Flask, Django, otros  ](advanced/wsgi/)
      * [ Genera Clientes  ](advanced/generate-clients/)
    * [ FastAPI CLI  ](fastapi-cli/)
    * [ Despliegue  ](deployment/)

Despliegue

      * [ Sobre las versiones de FastAPI  ](deployment/versions/)
      * [ Sobre HTTPS  ](deployment/https/)
      * [ Ejecutar un Servidor Manualmente  ](deployment/manually/)
      * [ Conceptos de Implementación  ](deployment/concepts/)
      * [ Despliega FastAPI en Proveedores de Nube  ](deployment/cloud/)
      * [ Servidores Workers - Uvicorn con Workers  ](deployment/server-workers/)
      * [ FastAPI en Contenedores - Docker  ](deployment/docker/)
    * [ How To - Recetas  ](how-to/)

How To - Recetas

      * [ General - Cómo Hacer - Recetas  ](how-to/general/)
      * [ GraphQL  ](how-to/graphql/)
      * [ Clase personalizada de Request y APIRoute  ](how-to/custom-request-and-route/)
      * [ OpenAPI Condicional  ](how-to/conditional-openapi/)
      * [ Extender OpenAPI  ](how-to/extending-openapi/)
      * [ Separación de Esquemas OpenAPI para Entrada y Salida o No  ](how-to/separate-openapi-schemas/)
      * [ Recursos Estáticos Personalizados para la Docs UI (Self-Hosting)  ](how-to/custom-docs-ui-assets/)
      * [ Configurar Swagger UI  ](how-to/configure-swagger-ui/)
      * [ Probando una Base de Datos  ](how-to/testing-database/)
  * [ Reference  ](reference/)

Reference

    * [ `FastAPI` class  ](reference/fastapi/)
    * [ Request Parameters  ](reference/parameters/)
    * [ Status Codes  ](reference/status/)
    * [ `UploadFile` class  ](reference/uploadfile/)
    * [ Exceptions - `HTTPException` and `WebSocketException` ](reference/exceptions/)
    * [ Dependencies - `Depends()` and `Security()` ](reference/dependencies/)
    * [ `APIRouter` class  ](reference/apirouter/)
    * [ Background Tasks - `BackgroundTasks` ](reference/background/)
    * [ `Request` class  ](reference/request/)
    * [ WebSockets  ](reference/websockets/)
    * [ `HTTPConnection` class  ](reference/httpconnection/)
    * [ `Response` class  ](reference/response/)
    * [ Custom Response Classes - File, HTML, Redirect, Streaming, etc.  ](reference/responses/)
    * [ Middleware  ](reference/middleware/)
    * [ OpenAPI  ](reference/openapi/)

OpenAPI

      * [ OpenAPI `docs` ](reference/openapi/docs/)
      * [ OpenAPI `models` ](reference/openapi/models/)
    * [ Security Tools  ](reference/security/)
    * [ Encoders - `jsonable_encoder` ](reference/encoders/)
    * [ Static Files - `StaticFiles` ](reference/staticfiles/)
    * [ Templating - `Jinja2Templates` ](reference/templating/)
    * [ Test Client - `TestClient` ](reference/testclient/)
  * [ FastAPI People  ](fastapi-people/)
  * [ Recursos  ](resources/)

Recursos

    * [ Ayuda a FastAPI - Consigue Ayuda  ](help-fastapi/)
    * [ Development - Contributing  ](contributing/)
    * [ Plantilla Full Stack FastAPI  ](project-generation/)
    * [ External Links and Articles  ](external-links/)
    * [ FastAPI and friends newsletter  ](newsletter/)
    * [ Repository Management Tasks  ](management-tasks/)
  * [ Acerca de  ](about/)

Acerca de

    * [ Alternativas, Inspiración y Comparaciones  ](alternatives/)
    * [ Historia, Diseño y Futuro  ](history-design-future/)
    * [ Benchmarks  ](benchmarks/)
    * [ Repository Management  ](management/)
  * [ Release Notes  ](release-notes/)

Tabla de contenidos

  * Sponsors 
  * Opiniones 
  * **Typer** , el FastAPI de las CLIs 
  * Requisitos 
  * Instalación 
  * Ejemplo 
    * Créalo 
    * Córrelo 
    * Revísalo 
    * Documentación interactiva de la API 
    * Documentación de API Alternativa 
  * Actualización del Ejemplo 
    * Actualización de la Documentación Interactiva de la API 
    * Actualización de la Documentación Alternativa de la API 
    * Resumen 
  * Rendimiento 
  * Dependencias 
    * Dependencias `standard`
    * Sin Dependencias `standard`
    * Dependencias Opcionales Adicionales 
  * Licencia 

# FastAPI¶

[![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-
teal.png)](https://fastapi.tiangolo.com)

_FastAPI framework, alto rendimiento, fácil de aprender, rápido de programar,
listo para producción_

[
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master)
](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)
[ ![Coverage](https://coverage-
badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ](https://coverage-
badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi) [ ![Package
version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)
](https://pypi.org/project/fastapi) [ ![Supported Python
versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
](https://pypi.org/project/fastapi)

* * *

**Documentación** : <https://fastapi.tiangolo.com>

**Código Fuente** : <https://github.com/fastapi/fastapi>

* * *

FastAPI es un framework web moderno, rápido (de alto rendimiento), para
construir APIs con Python basado en las anotaciones de tipos estándar de
Python.

Las características clave son:

  * **Rápido** : Muy alto rendimiento, a la par con **NodeJS** y **Go** (gracias a Starlette y Pydantic). Uno de los frameworks Python más rápidos disponibles.
  * **Rápido de programar** : Aumenta la velocidad para desarrollar funcionalidades en aproximadamente un 200% a 300%. *
  * **Menos bugs** : Reduce en aproximadamente un 40% los errores inducidos por humanos (desarrolladores). *
  * **Intuitivo** : Gran soporte para editores. Autocompletado en todas partes. Menos tiempo depurando.
  * **Fácil** : Diseñado para ser fácil de usar y aprender. Menos tiempo leyendo documentación.
  * **Corto** : Minimiza la duplicación de código. Múltiples funcionalidades desde cada declaración de parámetro. Menos bugs.
  * **Robusto** : Obtén código listo para producción. Con documentación interactiva automática.
  * **Basado en estándares** : Basado (y completamente compatible) con los estándares abiertos para APIs: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (anteriormente conocido como Swagger) y [JSON Schema](https://json-schema.org/).

* estimación basada en pruebas con un equipo de desarrollo interno, construyendo aplicaciones de producción.

## Sponsors¶

[![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io?ref=fastapi
"BlockBee Cryptocurrency Payment Gateway")
[![](https://fastapi.tiangolo.com/img/sponsors/platform-
sh.png)](https://platform.sh/try-it-now/?utm_source=fastapi-
signup&utm_medium=banner&utm_campaign=FastAPI-signup-June-2023 "Build, run and
scale your apps on a modern, reliable, and secure PaaS.")
[![](https://fastapi.tiangolo.com/img/sponsors/porter.png)](https://www.porter.run
"Deploy FastAPI on AWS with a few clicks")
[![](https://fastapi.tiangolo.com/img/sponsors/bump-
sh.svg)](https://bump.sh/fastapi?utm_source=fastapi&utm_medium=referral&utm_campaign=sponsor
"Automate FastAPI documentation generation with Bump.sh")
[![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-
badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI
files")
[![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge
"Auth, user management and more for your B2B product")
[![](https://fastapi.tiangolo.com/img/sponsors/coherence.png)](https://www.withcoherence.com/?utm_medium=advertising&utm_source=fastapi&utm_campaign=website
"Coherence")
[![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png)](https://www.mongodb.com/developer/languages/python/python-
quickstart-
fastapi/?utm_campaign=fastapi_framework&utm_source=fastapi_sponsorship&utm_medium=web_referral
"Simplify Full Stack Development with FastAPI & MongoDB")
[![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-
gh "Zuplo: Scale, Protect, Document, and Monetize your FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com?utm_source=fastapi
"liblab - Generate SDKs from FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-
fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy
& scale any full-stack web app on Render. Focus on building apps, not infra.")
[![](https://fastapi.tiangolo.com/img/sponsors/haystack-
fastapi.svg)](https://github.com/deepset-ai/haystack/ "Build powerful search
from composable, open source building blocks")
[![](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/
"Pay as you go for market data")
[![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com?utm_source=fastapi+repo&utm_medium=github+sponsorship
"SDKs for your API | Speakeasy")
[![](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/
"Svix - Webhooks as a service")
[![](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral
"Stainless | Generate best-in-class SDKs")

[Otros sponsors](https://fastapi.tiangolo.com/fastapi-people/#sponsors)

## Opiniones¶

" _[...] Estoy usando **FastAPI** un montón estos días. [...] De hecho, estoy
planeando usarlo para todos los servicios de **ML de mi equipo en Microsoft**.
Algunos de ellos se están integrando en el núcleo del producto **Windows** y
algunos productos de **Office**._"

Kabir Khan - **Microsoft** [(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

" _Adoptamos el paquete **FastAPI** para crear un servidor **REST** que pueda
ser consultado para obtener **predicciones**. [para Ludwig]_"

Piero Molino, Yaroslav Dudin, y Sai Sumanth Miryala - **Uber**
[(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

" _ **Netflix** se complace en anunciar el lanzamiento de código abierto de
nuestro framework de orquestación de **gestión de crisis** : **Dispatch**!
[construido con **FastAPI** ]_"

Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix**
[(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

" _Estoy súper emocionado con **FastAPI**. ¡Es tan divertido!_"

Brian Okken - **[host del podcast Python
Bytes](https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-
wrongs?time_in_sec=855)**
[(ref)](https://twitter.com/brianokken/status/1112220079972728832)

* * *

" _Honestamente, lo que has construido parece súper sólido y pulido. En muchos
aspectos, es lo que quería que **Hug** fuera; es realmente inspirador ver a
alguien construir eso._"

Timothy Crosley - **[creador de Hug](https://github.com/hugapi/hug)**
[(ref)](https://news.ycombinator.com/item?id=19455465)

* * *

" _Si estás buscando aprender un **framework moderno** para construir APIs
REST, échale un vistazo a **FastAPI** [...] Es rápido, fácil de usar y fácil
de aprender [...]_"

" _Nos hemos cambiado a **FastAPI** para nuestras **APIs** [...] Creo que te
gustará [...]_"

Ines Montani - Matthew Honnibal - **[fundadores de Explosion
AI](https://explosion.ai) \- [creadores de spaCy](https://spacy.io)**
[(ref)](https://twitter.com/_inesmontani/status/1144173225322143744) \-
[(ref)](https://twitter.com/honnibal/status/1144031421859655680)

* * *

" _Si alguien está buscando construir una API de Python para producción,
altamente recomendaría **FastAPI**. Está **hermosamente diseñado** , es
**simple de usar** y **altamente escalable** , se ha convertido en un
**componente clave** en nuestra estrategia de desarrollo API primero y está
impulsando muchas automatizaciones y servicios como nuestro Ingeniero Virtual
TAC._"

Deon Pillsbury - **Cisco**
[(ref)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-
activity-6963242628536487936-trAp/)

* * *

## **Typer** , el FastAPI de las CLIs¶

[![](https://typer.tiangolo.com/img/logo-margin/logo-margin-
vector.svg)](https://typer.tiangolo.com)

Si estás construyendo una aplicación de CLI para ser usada en el terminal en
lugar de una API web, revisa [**Typer**](https://typer.tiangolo.com/).

**Typer** es el hermano pequeño de FastAPI. Y está destinado a ser el
**FastAPI de las CLIs**. ⌨️ 🚀

## Requisitos¶

FastAPI se apoya en hombros de gigantes:

  * [Starlette](https://www.starlette.io/) para las partes web.
  * [Pydantic](https://docs.pydantic.dev/) para las partes de datos.

## Instalación¶

Crea y activa un [entorno virtual](https://fastapi.tiangolo.com/virtual-
environments/) y luego instala FastAPI:

    
    
    $ pip install "fastapi[standard]"
    
    ---> 100%
    

**Nota** : Asegúrate de poner `"fastapi[standard]"` entre comillas para
asegurar que funcione en todas las terminales.

## Ejemplo¶

### Créalo¶

  * Crea un archivo `main.py` con:

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

O usa `async def`...

Si tu código usa `async` / `await`, usa `async def`:

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    async def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

**Nota** :

Si no lo sabes, revisa la sección _"¿Con prisa?"_ sobre [`async` y `await` en
la documentación](https://fastapi.tiangolo.com/async/#in-a-hurry).

### Córrelo¶

Corre el servidor con:

    
    
    $ fastapi dev main.py
    
     ╭────────── FastAPI CLI - Development mode ───────────╮
     │                                                     │
     │  Serving at: http://127.0.0.1:8000                  │
     │                                                     │
     │  API docs: http://127.0.0.1:8000/docs               │
     │                                                     │
     │  Running in development mode, for production use:   │
     │                                                     │
     │  fastapi run                                        │
     │                                                     │
     ╰─────────────────────────────────────────────────────╯
    
    INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [2248755] using WatchFiles
    INFO:     Started server process [2248757]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    

Acerca del comando `fastapi dev main.py`...

El comando `fastapi dev` lee tu archivo `main.py`, detecta la app **FastAPI**
en él y arranca un servidor usando [Uvicorn](https://www.uvicorn.org).

Por defecto, `fastapi dev` comenzará con auto-recarga habilitada para el
desarrollo local.

Puedes leer más sobre esto en la [documentación del CLI de
FastAPI](https://fastapi.tiangolo.com/fastapi-cli/).

### Revísalo¶

Abre tu navegador en <http://127.0.0.1:8000/items/5?q=somequery>.

Verás el response JSON como:

    
    
    {"item_id": 5, "q": "somequery"}
    

Ya creaste una API que:

  * Recibe requests HTTP en los _paths_ `/` y `/items/{item_id}`.
  * Ambos _paths_ toman _operaciones_ `GET` (también conocidas como métodos HTTP).
  * El _path_ `/items/{item_id}` tiene un _parámetro de path_ `item_id` que debe ser un `int`.
  * El _path_ `/items/{item_id}` tiene un _parámetro de query_ `q` opcional que es un `str`.

### Documentación interactiva de la API¶

Ahora ve a <http://127.0.0.1:8000/docs>.

Verás la documentación interactiva automática de la API (proporcionada por
[Swagger UI](https://github.com/swagger-api/swagger-ui)):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-
simple.png)

### Documentación de API Alternativa¶

Y ahora, ve a <http://127.0.0.1:8000/redoc>.

Verás la documentación alternativa automática (proporcionada por
[ReDoc](https://github.com/Rebilly/ReDoc)):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## Actualización del Ejemplo¶

Ahora modifica el archivo `main.py` para recibir un body desde un request
`PUT`.

Declara el body usando tipos estándar de Python, gracias a Pydantic.

    
    
    from typing import Union
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        price: float
        is_offer: Union[bool, None] = None
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    
    
    @app.put("/items/{item_id}")
    def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}
    

El servidor `fastapi dev` debería recargarse automáticamente.

### Actualización de la Documentación Interactiva de la API¶

Ahora ve a <http://127.0.0.1:8000/docs>.

  * La documentación interactiva de la API se actualizará automáticamente, incluyendo el nuevo body:

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

  * Haz clic en el botón "Try it out", te permite llenar los parámetros e interactuar directamente con la API:

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

  * Luego haz clic en el botón "Execute", la interfaz de usuario se comunicará con tu API, enviará los parámetros, obtendrá los resultados y los mostrará en la pantalla:

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### Actualización de la Documentación Alternativa de la API¶

Y ahora, ve a <http://127.0.0.1:8000/redoc>.

  * La documentación alternativa también reflejará el nuevo parámetro de query y body:

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### Resumen¶

En resumen, declaras **una vez** los tipos de parámetros, body, etc. como
parámetros de función.

Lo haces con tipos estándar modernos de Python.

No tienes que aprender una nueva sintaxis, los métodos o clases de un paquete
específico, etc.

Solo **Python** estándar.

Por ejemplo, para un `int`:

    
    
    item_id: int
    

o para un modelo `Item` más complejo:

    
    
    item: Item
    

...y con esa única declaración obtienes:

  * Soporte para editores, incluyendo:
    * Autocompletado.
    * Chequeo de tipos.
  * Validación de datos:
    * Errores automáticos y claros cuando los datos son inválidos.
    * Validación incluso para objetos JSON profundamente anidados.
  * Conversión de datos de entrada: de la red a los datos y tipos de Python. Leyendo desde:
    * JSON.
    * Parámetros de path.
    * Parámetros de query.
    * Cookies.
    * Headers.
    * Forms.
    * Archivos.
  * Conversión de datos de salida: convirtiendo de datos y tipos de Python a datos de red (como JSON):
    * Convertir tipos de Python (`str`, `int`, `float`, `bool`, `list`, etc).
    * Objetos `datetime`.
    * Objetos `UUID`.
    * Modelos de base de datos.
    * ...y muchos más.
  * Documentación interactiva automática de la API, incluyendo 2 interfaces de usuario alternativas:
    * Swagger UI.
    * ReDoc.

* * *

Volviendo al ejemplo de código anterior, **FastAPI** :

  * Validará que haya un `item_id` en el path para requests `GET` y `PUT`.
  * Validará que el `item_id` sea del tipo `int` para requests `GET` y `PUT`.
    * Si no lo es, el cliente verá un error útil y claro.
  * Comprobará si hay un parámetro de query opcional llamado `q` (como en `http://127.0.0.1:8000/items/foo?q=somequery`) para requests `GET`.
    * Como el parámetro `q` está declarado con `= None`, es opcional.
    * Sin el `None` sería requerido (como lo es el body en el caso con `PUT`).
  * Para requests `PUT` a `/items/{item_id}`, leerá el body como JSON:
    * Comprobará que tiene un atributo requerido `name` que debe ser un `str`.
    * Comprobará que tiene un atributo requerido `price` que debe ser un `float`.
    * Comprobará que tiene un atributo opcional `is_offer`, que debe ser un `bool`, si está presente.
    * Todo esto también funcionaría para objetos JSON profundamente anidados.
  * Convertirá de y a JSON automáticamente.
  * Documentará todo con OpenAPI, que puede ser usado por:
    * Sistemas de documentación interactiva.
    * Sistemas de generación automática de código cliente, para muchos lenguajes.
  * Proporcionará 2 interfaces web de documentación interactiva directamente.

* * *

Solo tocamos los conceptos básicos, pero ya te haces una idea de cómo funciona
todo.

Intenta cambiar la línea con:

    
    
        return {"item_name": item.name, "item_id": item_id}
    

...desde:

    
    
            ... "item_name": item.name ...
    

...a:

    
    
            ... "item_price": item.price ...
    

...y observa cómo tu editor autocompleta los atributos y conoce sus tipos:

![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

Para un ejemplo más completo incluyendo más funcionalidades, ve al [Tutorial -
Guía del Usuario](https://fastapi.tiangolo.com/tutorial/).

**Alerta de spoilers** : el tutorial - guía del usuario incluye:

  * Declaración de **parámetros** desde otros lugares diferentes como: **headers** , **cookies** , **campos de formulario** y **archivos**.
  * Cómo establecer **restricciones de validación** como `maximum_length` o `regex`.
  * Un sistema de **Inyección de Dependencias** muy poderoso y fácil de usar.
  * Seguridad y autenticación, incluyendo soporte para **OAuth2** con **tokens JWT** y autenticación **HTTP Basic**.
  * Técnicas más avanzadas (pero igualmente fáciles) para declarar **modelos JSON profundamente anidados** (gracias a Pydantic).
  * Integración con **GraphQL** usando [Strawberry](https://strawberry.rocks) y otros paquetes.
  * Muchas funcionalidades extra (gracias a Starlette) como:
    * **WebSockets**
    * pruebas extremadamente fáciles basadas en HTTPX y `pytest`
    * **CORS**
    * **Sesiones de Cookies**
    * ...y más.

## Rendimiento¶

Benchmarks independientes de TechEmpower muestran aplicaciones **FastAPI**
ejecutándose bajo Uvicorn como [uno de los frameworks Python más rápidos
disponibles](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7),
solo por debajo de Starlette y Uvicorn (usados internamente por FastAPI). (*)

Para entender más sobre esto, ve la sección
[Benchmarks](https://fastapi.tiangolo.com/benchmarks/).

## Dependencias¶

FastAPI depende de Pydantic y Starlette.

### Dependencias `standard`¶

Cuando instalas FastAPI con `pip install "fastapi[standard]"` viene con el
grupo `standard` de dependencias opcionales:

Usadas por Pydantic:

  * [`email-validator`](https://github.com/JoshData/python-email-validator) \- para validación de correos electrónicos.

Usadas por Starlette:

  * [`httpx`](https://www.python-httpx.org) \- Requerido si deseas usar el `TestClient`.
  * [`jinja2`](https://jinja.palletsprojects.com) \- Requerido si deseas usar la configuración de plantilla predeterminada.
  * [`python-multipart`](https://github.com/Kludex/python-multipart) \- Requerido si deseas soportar "parsing" de forms, con `request.form()`.

Usadas por FastAPI / Starlette:

  * [`uvicorn`](https://www.uvicorn.org) \- para el servidor que carga y sirve tu aplicación. Esto incluye `uvicorn[standard]`, que incluye algunas dependencias (por ejemplo, `uvloop`) necesarias para servir con alto rendimiento.
  * `fastapi-cli` \- para proporcionar el comando `fastapi`.

### Sin Dependencias `standard`¶

Si no deseas incluir las dependencias opcionales `standard`, puedes instalar
con `pip install fastapi` en lugar de `pip install "fastapi[standard]"`.

### Dependencias Opcionales Adicionales¶

Existen algunas dependencias adicionales que podrías querer instalar.

Dependencias opcionales adicionales de Pydantic:

  * [`pydantic-settings`](https://docs.pydantic.dev/latest/usage/pydantic_settings/) \- para la gestión de configuraciones.
  * [`pydantic-extra-types`](https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/) \- para tipos extra para ser usados con Pydantic.

Dependencias opcionales adicionales de FastAPI:

  * [`orjson`](https://github.com/ijl/orjson) \- Requerido si deseas usar `ORJSONResponse`.
  * [`ujson`](https://github.com/esnme/ultrajson) \- Requerido si deseas usar `UJSONResponse`.

## Licencia¶

Este proyecto tiene licencia bajo los términos de la licencia MIT.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!

Volver al principio

  *[Completion]: also known as auto-complete, autocompletion, IntelliSense
  *[CLI]: Interfaz de Línea de Comandos
  *[Conversion]: also known as: serialization, parsing, marshalling
  *[Dependency Injection]: Dependency Injection – Einbringen von Abhängigkeiten: Auch bekannt als Komponenten, Ressourcen, Provider, Services, Injectables
  *["parsing"]: convertir el string que viene de un request HTTP en datos de Python
  *[tip məsləhətlərinə]: Tip Məsləhətləri: Type Hints
  *[otomatik tamamlama]: auto-complete, autocompletion, IntelliSense olaraq da bilinir
  *[_yollarında_]: Yol: Path 
  *[gövdə]: Gövdə: Body 
  *[çevirmək]: Çevrilmə: serialization, parsing, marshalling olaraq da bilinir
  *[Yol]: Yol: Path
  *[Sorğu]: Sorğu: Query
  *[Çərəzlər]: Çərəz: Cookie
  *[Başlıqlaq]: Başlıq: Header
  *[Formalar]: Forma: Form
  *[yolda]: Yol: Path
  *[məcburi olmayan]: Məcburi olmayan: Optional
  *[müştəri]: Müştəri: Client
  *[**başlıqlar**]: Başlıq: Header
  *[çərəzlər]: Çərəz: Cookie
  *[Müqayisələr]: Müqayisələr: Benchmarks
  *[şablon]: Şablon: Template
  *["çevirmə"]: HTTP sorğusu ilə alınan string məlumatın Python obyektinə çevrilməsi
  *[টাইপ্স]: একটি ভেরিয়েবল কি ধরনের ডেটা ধারণ করতে পারে।
  *[রূপান্তর]: যা পরিচিত: serialization, parsing, marshalling
  *[ডিপেন্ডেন্সি ইনজেকশন]: also known as components, resources, providers, services, injectables
  *[Code-Vervollständigung]: auch bekannt als Autovervollständigung, Autocompletion, IntelliSense
  *[ASGI]: Asynchronous Server Gateway Interface – Asynchrone Server-Verbindungsschnittstelle
  *[Body]: Body – Körper, Inhalt: Der eigentliche Inhalt einer Nachricht, nicht die Metadaten
  *[Konvertierung]: auch bekannt als: Serialisierung, Parsen, Marshalling
  *[„parsen“]: Konvertieren des Strings, der aus einer HTTP-Anfrage stammt, nach Python-Daten
  *[Autocompletado]: también conocido como autocompletado, IntelliSense
  *[Conversión]: también conocido como: serialización, parsing, marshalling
  *[Inyección de Dependencias]: también conocido como componentes, recursos, proveedores, servicios, inyectables



---

# https://fastapi.tiangolo.com/fa/



[ ![logo](img/icon-white.svg) ](. "FastAPI") FastAPI

[ fastapi/fastapi  ](https://github.com/fastapi/fastapi "رفتن به مخزن")

  * FastAPI  [ FastAPI  ](.) فهرست موضوعات 
    * اسپانسرهای طلایی 
    * نظر دیگران در مورد FastAPI 
    * **Typer** , فریم‌ورکی معادل FastAPI برای کار با واسط خط فرمان
    * نیازمندی‌ها 
    * نصب 
    * مثال 
      * ایجاد کنید 
      * اجرا کنید 
      * بررسی کنید 
      * مستندات API تعاملی 
      * مستندات API جایگزین 
    * تغییر مثال 
      * تغییر مستندات API تعاملی 
      * تغییر مستندات API جایگزین 
      * خلاصه 
    * کارایی 
    * نیازمندی‌های اختیاری 
    * لایسنس 
  * [ ویژگی ها  ](features/)
  * [ Learn  ](learn/)

Learn

    * [ Python Types Intro  ](python-types/)
    * [ Concurrency and async / await  ](async/)
    * [ Environment Variables  ](environment-variables/)
    * [ Virtual Environments  ](virtual-environments/)
    * [ Tutorial - User Guide  ](tutorial/)

Tutorial - User Guide

      * [ First Steps  ](tutorial/first-steps/)
      * [ Path Parameters  ](tutorial/path-params/)
      * [ Query Parameters  ](tutorial/query-params/)
      * [ Request Body  ](tutorial/body/)
      * [ Query Parameters and String Validations  ](tutorial/query-params-str-validations/)
      * [ Path Parameters and Numeric Validations  ](tutorial/path-params-numeric-validations/)
      * [ Query Parameter Models  ](tutorial/query-param-models/)
      * [ Body - Multiple Parameters  ](tutorial/body-multiple-params/)
      * [ Body - Fields  ](tutorial/body-fields/)
      * [ Body - Nested Models  ](tutorial/body-nested-models/)
      * [ Declare Request Example Data  ](tutorial/schema-extra-example/)
      * [ Extra Data Types  ](tutorial/extra-data-types/)
      * [ Cookie Parameters  ](tutorial/cookie-params/)
      * [ Header Parameters  ](tutorial/header-params/)
      * [ Cookie Parameter Models  ](tutorial/cookie-param-models/)
      * [ Header Parameter Models  ](tutorial/header-param-models/)
      * [ Response Model - Return Type  ](tutorial/response-model/)
      * [ Extra Models  ](tutorial/extra-models/)
      * [ Response Status Code  ](tutorial/response-status-code/)
      * [ Form Data  ](tutorial/request-forms/)
      * [ Form Models  ](tutorial/request-form-models/)
      * [ Request Files  ](tutorial/request-files/)
      * [ Request Forms and Files  ](tutorial/request-forms-and-files/)
      * [ Handling Errors  ](tutorial/handling-errors/)
      * [ Path Operation Configuration  ](tutorial/path-operation-configuration/)
      * [ JSON Compatible Encoder  ](tutorial/encoder/)
      * [ Body - Updates  ](tutorial/body-updates/)
      * [ Dependencies  ](tutorial/dependencies/)

Dependencies

        * [ Classes as Dependencies  ](tutorial/dependencies/classes-as-dependencies/)
        * [ Sub-dependencies  ](tutorial/dependencies/sub-dependencies/)
        * [ Dependencies in path operation decorators  ](tutorial/dependencies/dependencies-in-path-operation-decorators/)
        * [ Global Dependencies  ](tutorial/dependencies/global-dependencies/)
        * [ Dependencies with yield  ](tutorial/dependencies/dependencies-with-yield/)
      * [ امنیت  ](tutorial/security/)

امنیت

        * [ Security - First Steps  ](tutorial/security/first-steps/)
        * [ Get Current User  ](tutorial/security/get-current-user/)
        * [ Simple OAuth2 with Password and Bearer  ](tutorial/security/simple-oauth2/)
        * [ OAuth2 with Password (and hashing), Bearer with JWT tokens  ](tutorial/security/oauth2-jwt/)
      * [ میان‌افزار - middleware  ](tutorial/middleware/)
      * [ CORS (Cross-Origin Resource Sharing)  ](tutorial/cors/)
      * [ SQL (Relational) Databases  ](tutorial/sql-databases/)
      * [ Bigger Applications - Multiple Files  ](tutorial/bigger-applications/)
      * [ Background Tasks  ](tutorial/background-tasks/)
      * [ Metadata and Docs URLs  ](tutorial/metadata/)
      * [ Static Files  ](tutorial/static-files/)
      * [ Testing  ](tutorial/testing/)
      * [ Debugging  ](tutorial/debugging/)
    * [ Advanced User Guide  ](advanced/)

Advanced User Guide

      * [ Path Operation Advanced Configuration  ](advanced/path-operation-advanced-configuration/)
      * [ Additional Status Codes  ](advanced/additional-status-codes/)
      * [ Return a Response Directly  ](advanced/response-directly/)
      * [ Custom Response - HTML, Stream, File, others  ](advanced/custom-response/)
      * [ Additional Responses in OpenAPI  ](advanced/additional-responses/)
      * [ Response Cookies  ](advanced/response-cookies/)
      * [ Response Headers  ](advanced/response-headers/)
      * [ Response - Change Status Code  ](advanced/response-change-status-code/)
      * [ Advanced Dependencies  ](advanced/advanced-dependencies/)
      * [ Advanced Security  ](advanced/security/)

Advanced Security

        * [ OAuth2 scopes  ](advanced/security/oauth2-scopes/)
        * [ HTTP Basic Auth  ](advanced/security/http-basic-auth/)
      * [ Using the Request Directly  ](advanced/using-request-directly/)
      * [ Using Dataclasses  ](advanced/dataclasses/)
      * [ Advanced Middleware  ](advanced/middleware/)
      * [ زیر برنامه ها - اتصال  ](advanced/sub-applications/)
      * [ Behind a Proxy  ](advanced/behind-a-proxy/)
      * [ Templates  ](advanced/templates/)
      * [ WebSockets  ](advanced/websockets/)
      * [ Lifespan Events  ](advanced/events/)
      * [ Testing WebSockets  ](advanced/testing-websockets/)
      * [ Testing Events: startup - shutdown  ](advanced/testing-events/)
      * [ Testing Dependencies with Overrides  ](advanced/testing-dependencies/)
      * [ Async Tests  ](advanced/async-tests/)
      * [ Settings and Environment Variables  ](advanced/settings/)
      * [ OpenAPI Callbacks  ](advanced/openapi-callbacks/)
      * [ OpenAPI Webhooks  ](advanced/openapi-webhooks/)
      * [ Including WSGI - Flask, Django, others  ](advanced/wsgi/)
      * [ Generate Clients  ](advanced/generate-clients/)
    * [ FastAPI CLI  ](fastapi-cli/)
    * [ Deployment  ](deployment/)

Deployment

      * [ About FastAPI versions  ](deployment/versions/)
      * [ About HTTPS  ](deployment/https/)
      * [ Run a Server Manually  ](deployment/manually/)
      * [ Deployments Concepts  ](deployment/concepts/)
      * [ Deploy FastAPI on Cloud Providers  ](deployment/cloud/)
      * [ Server Workers - Uvicorn with Workers  ](deployment/server-workers/)
      * [ FastAPI in Containers - Docker  ](deployment/docker/)
    * [ How To - Recipes  ](how-to/)

How To - Recipes

      * [ General - How To - Recipes  ](how-to/general/)
      * [ GraphQL  ](how-to/graphql/)
      * [ Custom Request and APIRoute class  ](how-to/custom-request-and-route/)
      * [ Conditional OpenAPI  ](how-to/conditional-openapi/)
      * [ Extending OpenAPI  ](how-to/extending-openapi/)
      * [ Separate OpenAPI Schemas for Input and Output or Not  ](how-to/separate-openapi-schemas/)
      * [ Custom Docs UI Static Assets (Self-Hosting)  ](how-to/custom-docs-ui-assets/)
      * [ Configure Swagger UI  ](how-to/configure-swagger-ui/)
      * [ Testing a Database  ](how-to/testing-database/)
  * [ Reference  ](reference/)

Reference

    * [ `FastAPI` class  ](reference/fastapi/)
    * [ Request Parameters  ](reference/parameters/)
    * [ Status Codes  ](reference/status/)
    * [ `UploadFile` class  ](reference/uploadfile/)
    * [ Exceptions - `HTTPException` and `WebSocketException` ](reference/exceptions/)
    * [ Dependencies - `Depends()` and `Security()` ](reference/dependencies/)
    * [ `APIRouter` class  ](reference/apirouter/)
    * [ Background Tasks - `BackgroundTasks` ](reference/background/)
    * [ `Request` class  ](reference/request/)
    * [ WebSockets  ](reference/websockets/)
    * [ `HTTPConnection` class  ](reference/httpconnection/)
    * [ `Response` class  ](reference/response/)
    * [ Custom Response Classes - File, HTML, Redirect, Streaming, etc.  ](reference/responses/)
    * [ Middleware  ](reference/middleware/)
    * [ OpenAPI  ](reference/openapi/)

OpenAPI

      * [ OpenAPI `docs` ](reference/openapi/docs/)
      * [ OpenAPI `models` ](reference/openapi/models/)
    * [ Security Tools  ](reference/security/)
    * [ Encoders - `jsonable_encoder` ](reference/encoders/)
    * [ Static Files - `StaticFiles` ](reference/staticfiles/)
    * [ Templating - `Jinja2Templates` ](reference/templating/)
    * [ Test Client - `TestClient` ](reference/testclient/)
  * [ FastAPI People  ](fastapi-people/)
  * [ Resources  ](resources/)

Resources

    * [ Help FastAPI - Get Help  ](help-fastapi/)
    * [ Development - Contributing  ](contributing/)
    * [ Full Stack FastAPI Template  ](project-generation/)
    * [ External Links and Articles  ](external-links/)
    * [ FastAPI and friends newsletter  ](newsletter/)
    * [ Repository Management Tasks  ](management-tasks/)
  * [ About  ](about/)

About

    * [ Alternatives, Inspiration and Comparisons  ](alternatives/)
    * [ History, Design and Future  ](history-design-future/)
    * [ Benchmarks  ](benchmarks/)
    * [ Repository Management  ](management/)
  * [ Release Notes  ](release-notes/)

فهرست موضوعات

  * اسپانسرهای طلایی 
  * نظر دیگران در مورد FastAPI 
  * **Typer** , فریم‌ورکی معادل FastAPI برای کار با واسط خط فرمان
  * نیازمندی‌ها 
  * نصب 
  * مثال 
    * ایجاد کنید 
    * اجرا کنید 
    * بررسی کنید 
    * مستندات API تعاملی 
    * مستندات API جایگزین 
  * تغییر مثال 
    * تغییر مستندات API تعاملی 
    * تغییر مستندات API جایگزین 
    * خلاصه 
  * کارایی 
  * نیازمندی‌های اختیاری 
  * لایسنس 

# FastAPI¶

[![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-
teal.png)](https://fastapi.tiangolo.com)

_فریم‌ورک FastAPI، کارایی بالا، یادگیری آسان، کدنویسی سریع، آماده برای استفاده
در محیط پروداکشن_

[ ![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg)
](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest) [
![Coverage](https://img.shields.io/codecov/c/github/fastapi/fastapi?color=%2334D058)
](https://codecov.io/gh/fastapi/fastapi) [ ![Package
version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)
](https://pypi.org/project/fastapi) [ ![Supported Python
versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
](https://pypi.org/project/fastapi)

* * *

**مستندات** : <https://fastapi.tiangolo.com>

**کد منبع** : <https://github.com/fastapi/fastapi>

* * *

FastAPI یک وب فریم‌ورک مدرن و سریع (با کارایی بالا) برای ایجاد APIهای متنوع
(وب، وب‌سوکت و غبره) با زبان پایتون نسخه +۳.۶ است. این فریم‌ورک با رعایت کامل
راهنمای نوع داده (Type Hint) ایجاد شده است.

ویژگی‌های کلیدی این فریم‌ورک عبارتند از:

  * **سرعت** : کارایی بسیار بالا و قابل مقایسه با **NodeJS** و **Go** (با تشکر از Starlette و Pydantic). یکی از سریع‌ترین فریم‌ورک‌های پایتونی موجود.

  * **کدنویسی سریع** : افزایش ۲۰۰ تا ۳۰۰ درصدی سرعت توسعه قابلیت‌های جدید. *

  * **باگ کمتر** : کاهش ۴۰ درصدی خطاهای انسانی (برنامه‌نویسی). *
  * **هوشمندانه** : پشتیبانی فوق‌العاده در محیط‌های توسعه یکپارچه (IDE). تکمیل در همه بخش‌های کد. کاهش زمان رفع باگ.
  * **آسان** : طراحی شده برای یادگیری و استفاده آسان. کاهش زمان مورد نیاز برای مراجعه به مستندات.
  * **کوچک** : کاهش تکرار در کد. چندین قابلیت برای هر پارامتر (منظور پارامترهای ورودی تابع هندلر می‌باشد، به بخش [خلاصه](https://fastapi.tiangolo.com/#recap) در همین صفحه مراجعه شود). باگ کمتر.
  * **استوار** : ایجاد کدی آماده برای استفاده در محیط پروداکشن و تولید خودکار مستندات تعاملی
  * **مبتنی بر استانداردها** : مبتنی بر (و منطبق با) استانداردهای متن باز مربوط به API: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (سوگر سابق) و [JSON Schema](https://json-schema.org/).

* تخمین‌ها بر اساس تست‌های انجام شده در یک تیم توسعه داخلی که مشغول ایجاد برنامه‌های کاربردی واقعی بودند صورت گرفته است.

## اسپانسرهای طلایی¶

[![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io?ref=fastapi
"BlockBee Cryptocurrency Payment Gateway")
[![](https://fastapi.tiangolo.com/img/sponsors/platform-
sh.png)](https://platform.sh/try-it-now/?utm_source=fastapi-
signup&utm_medium=banner&utm_campaign=FastAPI-signup-June-2023 "Build, run and
scale your apps on a modern, reliable, and secure PaaS.")
[![](https://fastapi.tiangolo.com/img/sponsors/porter.png)](https://www.porter.run
"Deploy FastAPI on AWS with a few clicks")
[![](https://fastapi.tiangolo.com/img/sponsors/bump-
sh.svg)](https://bump.sh/fastapi?utm_source=fastapi&utm_medium=referral&utm_campaign=sponsor
"Automate FastAPI documentation generation with Bump.sh")
[![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-
badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI
files")
[![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge
"Auth, user management and more for your B2B product")
[![](https://fastapi.tiangolo.com/img/sponsors/coherence.png)](https://www.withcoherence.com/?utm_medium=advertising&utm_source=fastapi&utm_campaign=website
"Coherence")
[![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png)](https://www.mongodb.com/developer/languages/python/python-
quickstart-
fastapi/?utm_campaign=fastapi_framework&utm_source=fastapi_sponsorship&utm_medium=web_referral
"Simplify Full Stack Development with FastAPI & MongoDB")
[![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-
gh "Zuplo: Scale, Protect, Document, and Monetize your FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com?utm_source=fastapi
"liblab - Generate SDKs from FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-
fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy
& scale any full-stack web app on Render. Focus on building apps, not infra.")

[دیگر اسپانسرها](https://fastapi.tiangolo.com/fastapi-people/#sponsors)

## نظر دیگران در مورد FastAPI¶

_[...] I'm using **FastAPI** a ton these days. [...] I'm actually planning to
use it for all of my team's **ML services at Microsoft**. Some of them are
getting integrated into the core **Windows** product and some **Office**
products."_

Kabir Khan - **Microsoft** [(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

_"We adopted the **FastAPI** library to spawn a **REST** server that can be
queried to obtain **predictions**. [for Ludwig]"_

Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - **Uber**
[(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

" **Netflix** is pleased to announce the open-source release of our **crisis
management** orchestration framework: **Dispatch**! [built with **FastAPI** ]"

Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix**
[(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

" _I’m over the moon excited about **FastAPI**. It’s so fun!"_

Brian Okken - **[Python Bytes](https://pythonbytes.fm/episodes/show/123/time-
to-right-the-py-wrongs?time_in_sec=855) podcast host**
[(ref)](https://twitter.com/brianokken/status/1112220079972728832)

* * *

" _Honestly, what you've built looks super solid and polished. In many ways,
it's what I wanted **Hug** to be - it's really inspiring to see someone build
that."_

Timothy Crosley - **[Hug](https://github.com/hugapi/hug) creator**
[(ref)](https://news.ycombinator.com/item?id=19455465)

* * *

" _If you're looking to learn one **modern framework** for building REST APIs,
check out **FastAPI** [...] It's fast, easy to use and easy to learn [...]"_

" _We've switched over to **FastAPI** for our **APIs** [...] I think you'll
like it [...]_"

Ines Montani - Matthew Honnibal - **[Explosion AI](https://explosion.ai)
founders - [spaCy](https://spacy.io) creators**
[(ref)](https://twitter.com/_inesmontani/status/1144173225322143744) \-
[(ref)](https://twitter.com/honnibal/status/1144031421859655680)

* * *

## **Typer** , فریم‌ورکی معادل FastAPI برای کار با واسط خط فرمان¶

[![](https://typer.tiangolo.com/img/logo-margin/logo-margin-
vector.svg)](https://typer.tiangolo.com)

اگر در حال ساختن برنامه‌ای برای استفاده در CLI (به جای استفاده در وب) هستید،
می‌توانید از [**Typer**](https://typer.tiangolo.com/). استفاده کنید.

**Typer** دوقلوی کوچکتر FastAPI است و قرار است معادلی برای FastAPI در
برنامه‌های CLI باشد.️ 🚀

## نیازمندی‌ها¶

پایتون +۳.۶

FastAPI مبتنی بر ابزارهای قدرتمند زیر است:

  * فریم‌ورک [Starlette](https://www.starlette.io/) برای بخش وب.
  * کتابخانه [Pydantic](https://docs.pydantic.dev/) برای بخش داده‌.

## نصب¶

    
    
    $ pip install fastapi
    
    ---> 100%
    

نصب یک سرور پروداکشن نظیر [Uvicorn](https://www.uvicorn.org) یا
[Hypercorn](https://github.com/pgjones/hypercorn) نیز جزء نیازمندی‌هاست.

    
    
    $ pip install "uvicorn[standard]"
    
    ---> 100%
    

## مثال¶

### ایجاد کنید¶

  * فایلی به نام `main.py` با محتوای زیر ایجاد کنید:

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

همچنین می‌توانید از `async def`... نیز استفاده کنید

اگر در کدتان از `async` / `await` استفاده می‌کنید، از `async def` برای تعریف
تابع خود استفاده کنید:

    
    
    from typing import Optional
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    async def read_item(item_id: int, q: Optional[str] = None):
        return {"item_id": item_id, "q": q}
    

**توجه** :

اگر با `async / await` آشنا نیستید، به بخش _"عجله‌ دارید?"_ در صفحه درباره
[`async` و `await` در مستندات](https://fastapi.tiangolo.com/async/#in-a-hurry)
مراجعه کنید.

### اجرا کنید¶

با استفاده از دستور زیر سرور را اجرا کنید:

    
    
    $ uvicorn main:app --reload
    
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [28720]
    INFO:     Started server process [28722]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    

درباره دستور `uvicorn main:app --reload`...

دستور `uvicorn main:app` شامل موارد زیر است:

  * `main`: فایل `main.py` (ماژول پایتون ایجاد شده).
  * `app`: شیء ایجاد شده در فایل `main.py` در خط `app = FastAPI()`.
  * `--reload`: ریستارت کردن سرور با تغییر کد. تنها در هنگام توسعه از این گزینه استفاده شود..

### بررسی کنید¶

آدرس <http://127.0.0.1:8000/items/5?q=somequery> را در مرورگر خود باز کنید.

پاسخ JSON زیر را مشاهده خواهید کرد:

    
    
    {"item_id": 5, "q": "somequery"}
    

تا اینجا شما APIای ساختید که:

  * درخواست‌های HTTP به _مسیرهای_ `/` و `/items/{item_id}` را دریافت می‌کند.
  * هردو _مسیر_ عملیات (یا HTTP _متد_ ) `GET` را پشتیبانی می‌کند.
  * _مسیر_ `/items/{item_id}` شامل _پارامتر مسیر_ `item_id` از نوع `int` است.
  * _مسیر_ `/items/{item_id}` شامل _پارامتر پرسمان_ اختیاری `q` از نوع `str` است.

### مستندات API تعاملی¶

حال به آدرس <http://127.0.0.1:8000/docs> بروید.

مستندات API تعاملی (ایجاد شده به کمک [Swagger UI](https://github.com/swagger-
api/swagger-ui)) را مشاهده خواهید کرد:

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-
simple.png)

### مستندات API جایگزین¶

حال به آدرس <http://127.0.0.1:8000/redoc> بروید.

مستندات خودکار دیگری را مشاهده خواهید کرد که به کمک
[ReDoc](https://github.com/Rebilly/ReDoc) ایجاد می‌شود:

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## تغییر مثال¶

حال فایل `main.py` را مطابق زیر ویرایش کنید تا بتوانید بدنه یک درخواست `PUT`
را دریافت کنید.

به کمک Pydantic بدنه درخواست را با انواع استاندارد پایتون تعریف کنید.

    
    
    from typing import Optional
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        price: float
        is_offer: Union[bool, None] = None
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    
    
    @app.put("/items/{item_id}")
    def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}
    

سرور به صورت خودکار ری‌استارت می‌شود (زیرا پیشتر از گزینه `--reload` در دستور
`uvicorn` استفاده کردیم).

### تغییر مستندات API تعاملی¶

مجددا به آدرس <http://127.0.0.1:8000/docs> بروید.

  * مستندات API تعاملی به صورت خودکار به‌روز شده است و شامل بدنه تعریف شده در مرحله قبل است:

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

  * روی دکمه "Try it out" کلیک کنید، اکنون می‌توانید پارامترهای مورد نیاز هر API را مشخص کرده و به صورت مستقیم با آنها تعامل کنید:

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

  * سپس روی دکمه "Execute" کلیک کنید، خواهید دید که واسط کاربری با APIهای تعریف شده ارتباط برقرار کرده، پارامترهای مورد نیاز را به آن‌ها ارسال می‌کند، سپس نتایج را دریافت کرده و در صفحه نشان می‌دهد:

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### تغییر مستندات API جایگزین¶

حال به آدرس <http://127.0.0.1:8000/redoc> بروید.

  * خواهید دید که مستندات جایگزین نیز به‌روزرسانی شده و شامل پارامتر پرسمان و بدنه تعریف شده می‌باشد:

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### خلاصه¶

به طور خلاصه شما **یک بار** انواع پارامترها، بدنه و غیره را به عنوان
پارامترهای ورودی تابع خود تعریف می‌کنید.

این کار را با استفاده از انواع استاندارد و مدرن موجود در پایتون انجام می‌دهید.

نیازی به یادگیری نحو جدید یا متدها و کلاس‌های یک کتابخانه بخصوص و غیره نیست.

تنها **پایتون +۳.۶**.

به عنوان مثال برای یک پارامتر از نوع `int`:

    
    
    item_id: int
    

یا برای یک مدل پیچیده‌تر مثل `Item`:

    
    
    item: Item
    

...و با همین اعلان تمامی قابلیت‌های زیر در دسترس قرار می‌گیرد:

  * پشتیبانی ویرایشگر متنی شامل:
    * تکمیل کد.
    * بررسی انواع داده.
  * اعتبارسنجی داده:
    * خطاهای خودکار و مشخص در هنگام نامعتبر بودن داده.
    * اعتبارسنجی، حتی برای اشیاء JSON تو در تو.
  * تبدیل داده ورودی: که از شبکه رسیده به انواع و داد‌ه‌ پایتونی. این داده‌ شامل:
    * JSON.
    * پارامترهای مسیر.
    * پارامترهای پرسمان.
    * کوکی‌ها.
    * سرآیند‌ها (هدرها).
    * فرم‌ها.
    * فایل‌ها.
  * تبدیل داده خروجی: تبدیل از انواع و داده‌ پایتون به داده شبکه (مانند JSON):
    * تبدیل انواع داده پایتونی (`str`, `int`, `float`, `bool`, `list` و غیره).
    * اشیاء `datetime`.
    * اشیاء `UUID`.
    * qمدل‌های پایگاه‌داده.
    * و موارد بیشمار دیگر.
  * دو مدل مستند API تعاملی خودکار :
    * Swagger UI.
    * ReDoc.

* * *

به مثال قبلی باز می‌گردیم، در این مثال **FastAPI** موارد زیر را انجام می‌دهد:

  * اعتبارسنجی اینکه پارامتر `item_id` در مسیر درخواست‌های `GET` و `PUT` موجود است.
  * اعتبارسنجی اینکه پارامتر `item_id` در درخواست‌های `GET` و `PUT` از نوع `int` است.
    * اگر غیر از این موارد باشد، سرویس‌گیرنده خطای مفید و مشخصی دریافت خواهد کرد.
  * بررسی وجود پارامتر پرسمان اختیاری `q` (مانند `http://127.0.0.1:8000/items/foo?q=somequery`) در درخواست‌های `GET`.
    * از آنجا که پارامتر `q` با `= None` مقداردهی شده است، این پارامتر اختیاری است.
    * اگر از مقدار اولیه `None` استفاده نکنیم، این پارامتر الزامی خواهد بود (همانند بدنه درخواست در درخواست `PUT`).
  * برای درخواست‌های `PUT` به آدرس `/items/{item_id}`، بدنه درخواست باید از نوع JSON تعریف شده باشد:
    * بررسی اینکه بدنه شامل فیلدی با نام `name` و از نوع `str` است.
    * بررسی اینکه بدنه شامل فیلدی با نام `price` و از نوع `float` است.
    * بررسی اینکه بدنه شامل فیلدی اختیاری با نام `is_offer` است، که در صورت وجود باید از نوع `bool` باشد.
    * تمامی این موارد برای اشیاء JSON در هر عمقی قابل بررسی می‌باشد.
  * تبدیل از/به JSON به صورت خودکار.
  * مستندسازی همه چیز با استفاده از OpenAPI، که می‌توان از آن برای موارد زیر استفاده کرد:
    * سیستم مستندات تعاملی.
    * تولید خودکار کد سرویس‌گیرنده‌ در زبان‌های برنامه‌نویسی بیشمار.
  * فراهم سازی ۲ مستند تعاملی مبتنی بر وب به صورت پیش‌فرض.

* * *

موارد ذکر شده تنها پاره‌ای از ویژگی‌های بیشمار FastAPI است اما ایده‌ای کلی از
طرز کار آن در اختیار قرار می‌دهد.

خط زیر را به این صورت تغییر دهید:

    
    
        return {"item_name": item.name, "item_id": item_id}
    

از:

    
    
            ... "item_name": item.name ...
    

به:

    
    
            ... "item_price": item.price ...
    

در حین تایپ کردن توجه کنید که چگونه ویرایش‌گر، ویژگی‌های کلاس `Item` را تشخیص
داده و به تکمیل خودکار آنها کمک می‌کند:

![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

برای مشاهده مثال‌های کامل‌تر که شامل قابلیت‌های بیشتری از FastAPI باشد به بخش
[آموزش - راهنمای کاربر](https://fastapi.tiangolo.com/tutorial/) مراجعه کنید.

**هشدار اسپویل** : بخش آموزش - راهنمای کاربر شامل موارد زیر است:

  * اعلان **پارامترهای** موجود در بخش‌های دیگر درخواست، شامل: **سرآیند‌ (هدر)ها** ، **کوکی‌ها** ، **فیلد‌های فرم** و **فایل‌ها**.
  * چگونگی تنظیم **محدودیت‌های اعتبارسنجی** به عنوان مثال `maximum_length` یا `regex`.
  * سیستم **Dependency Injection** قوی و کاربردی.
  * امنیت و تایید هویت, شامل پشتیبانی از **OAuth2** مبتنی بر **JWT tokens** و **HTTP Basic**.
  * تکنیک پیشرفته برای تعریف **مدل‌های چند سطحی JSON** (بر اساس Pydantic).
  * قابلیت‌های اضافی دیگر (بر اساس Starlette) شامل:
    * **وب‌سوکت**
    * **GraphQL**
    * تست‌های خودکار آسان مبتنی بر HTTPX و `pytest`
    * **CORS**
    * **Cookie Sessions**
    * و موارد بیشمار دیگر.

## کارایی¶

معیار (بنچمارک‌)های مستقل TechEmpower حاکی از آن است که برنامه‌های **FastAPI**
که تحت Uvicorn اجرا می‌شود، [یکی از سریع‌ترین فریم‌ورک‌های مبتنی بر
پایتون](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7)،
است که کمی ضعیف‌تر از Starlette و Uvicorn عمل می‌کند (فریم‌ورک و سروری که
FastAPI بر اساس آنها ایجاد شده است) (*)

برای درک بهتری از این موضوع به بخش
[بنچ‌مارک‌ها](https://fastapi.tiangolo.com/benchmarks/) مراجعه کنید.

## نیازمندی‌های اختیاری¶

استفاده شده توسط Pydantic:

  * [`email-validator`](https://github.com/JoshData/python-email-validator) \- برای اعتبارسنجی آدرس‌های ایمیل.

استفاده شده توسط Starlette:

  * [`HTTPX`](https://www.python-httpx.org) \- در صورتی که می‌خواهید از `TestClient` استفاده کنید.
  * [`aiofiles`](https://github.com/Tinche/aiofiles) \- در صورتی که می‌خواهید از `FileResponse` و `StaticFiles` استفاده کنید.
  * [`jinja2`](https://jinja.palletsprojects.com) \- در صورتی که بخواهید از پیکربندی پیش‌فرض برای قالب‌ها استفاده کنید.
  * [`python-multipart`](https://github.com/Kludex/python-multipart) \- در صورتی که بخواهید با استفاده از `request.form()` از قابلیت "تجزیه (parse)" فرم استفاده کنید.
  * [`itsdangerous`](https://pythonhosted.org/itsdangerous/) \- در صورتی که بخواید از `SessionMiddleware` پشتیبانی کنید.
  * [`pyyaml`](https://pyyaml.org/wiki/PyYAMLDocumentation) \- برای پشتیبانی `SchemaGenerator` در Starlet (به احتمال زیاد برای کار کردن با FastAPI به آن نیازی پیدا نمی‌کنید).
  * [`graphene`](https://graphene-python.org/) \- در صورتی که از `GraphQLApp` پشتیبانی می‌کنید.

استفاده شده توسط FastAPI / Starlette:

  * [`uvicorn`](https://www.uvicorn.org) \- برای سرور اجرا کننده برنامه وب.
  * [`orjson`](https://github.com/ijl/orjson) \- در صورتی که بخواهید از `ORJSONResponse` استفاده کنید.
  * [`ujson`](https://github.com/esnme/ultrajson) \- در صورتی که بخواهید از `UJSONResponse` استفاده کنید.

می‌توان همه این موارد را با استفاده از دستور `pip install fastapi[all]`. به
صورت یکجا نصب کرد.

## لایسنس¶

این پروژه مشمول قوانین و مقررات لایسنس MIT است.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!

برگشت به بالا

  *[Completion]: also known as auto-complete, autocompletion, IntelliSense
  *[CLI]: Command Line Interface
  *[Conversion]: also known as: serialization, parsing, marshalling
  *[Dependency Injection]: also known as components, resources, providers, services, injectables
  *["parsing"]: convertir el string que viene de un request HTTP en datos de Python
  *[tip məsləhətlərinə]: Tip Məsləhətləri: Type Hints
  *[otomatik tamamlama]: auto-complete, autocompletion, IntelliSense olaraq da bilinir
  *[_yollarında_]: Yol: Path 
  *[gövdə]: Gövdə: Body 
  *[çevirmək]: Çevrilmə: serialization, parsing, marshalling olaraq da bilinir
  *[Yol]: Yol: Path
  *[Sorğu]: Sorğu: Query
  *[Çərəzlər]: Çərəz: Cookie
  *[Başlıqlaq]: Başlıq: Header
  *[Formalar]: Forma: Form
  *[yolda]: Yol: Path
  *[məcburi olmayan]: Məcburi olmayan: Optional
  *[müştəri]: Müştəri: Client
  *[**başlıqlar**]: Başlıq: Header
  *[çərəzlər]: Çərəz: Cookie
  *[Müqayisələr]: Müqayisələr: Benchmarks
  *[şablon]: Şablon: Template
  *["çevirmə"]: HTTP sorğusu ilə alınan string məlumatın Python obyektinə çevrilməsi
  *[টাইপ্স]: একটি ভেরিয়েবল কি ধরনের ডেটা ধারণ করতে পারে।
  *[রূপান্তর]: যা পরিচিত: serialization, parsing, marshalling
  *[ডিপেন্ডেন্সি ইনজেকশন]: also known as components, resources, providers, services, injectables
  *[Code-Vervollständigung]: auch bekannt als Autovervollständigung, Autocompletion, IntelliSense
  *[ASGI]: Asynchronous Server Gateway Interface – Asynchrone Server-Verbindungsschnittstelle
  *[Body]: Body – Körper, Inhalt: Der eigentliche Inhalt einer Nachricht, nicht die Metadaten
  *[Konvertierung]: auch bekannt als: Serialisierung, Parsen, Marshalling
  *[„parsen“]: Konvertieren des Strings, der aus einer HTTP-Anfrage stammt, nach Python-Daten
  *[Autocompletado]: también conocido como autocompletado, IntelliSense
  *[Conversión]: también conocido como: serialización, parsing, marshalling
  *[Inyección de Dependencias]: también conocido como componentes, recursos, proveedores, servicios, inyectables
  *[واسط خط فرمان]: CLI (Command Line Interface)
  *[سرعت]: Fast
  *[کدنویسی سریع]: Fast to code
  *[باگ کمتر]: Fewer bugs
  *[هوشمندانه]: Intuitive
  *[تکمیل]: یا اتوکامپلیت، اتوکامپلشن، اینتلیسنس
  *[آسان]: Easy
  *[کوچک]: Short
  *[استوار]: Robust
  *[مستندات تعاملی]: Interactive documentation
  *[مبتنی بر استانداردها]: Standards-based
  *[عملیات]: operations در OpenAPI
  *[_پارامتر مسیر_]: Path Parameter
  *[_پارامتر پرسمان_]: Query Parameter
  *[بدنه]: Body
  *[انواع]: Type
  *[نحو]: Syntax
  *[تبدیل]: serialization, parsing, marshalling
  *[پارامترهای مسیر]: Path parameters
  *[پارامترهای پرسمان]: Query parameters
  *[کوکی‌ها]: Cookies
  *[سرآیند‌ها (هدرها)]: Headers
  *[فرم‌ها]: Forms
  *[فایل‌ها]: Files
  *[محدودیت‌های اعتبارسنجی]: Validation Constraints
  *[وب‌سوکت]: WebSocket
  *["تجزیه (parse)"]: تبدیل رشته متنی موجود در درخواست HTTP به انواع داده پایتون



---

# https://fastapi.tiangolo.com/fr/



[ ![logo](img/icon-white.svg) ](. "FastAPI") FastAPI

[ fastapi/fastapi  ](https://github.com/fastapi/fastapi "Aller au dépôt")

  * FastAPI  [ FastAPI  ](.) Table des matières 
    * Sponsors 
    * Opinions 
    * **Typer** , le FastAPI des CLI
    * Prérequis 
    * Installation 
    * Exemple 
      * Créez 
      * Lancez 
      * Vérifiez 
      * Documentation API interactive 
      * Documentation API alternative 
    * Exemple plus poussé 
      * Plus loin avec la documentation API interactive 
      * Plus loin avec la documentation API alternative 
      * En résumé 
    * Performance 
    * Dépendances facultatives 
    * Licence 
  * [ Fonctionnalités  ](features/)
  * [ Apprendre  ](learn/)

Apprendre

    * [ Introduction aux Types Python  ](python-types/)
    * [ Concurrence et les mots-clés async et await  ](async/)
    * [ Environment Variables  ](environment-variables/)
    * [ Virtual Environments  ](virtual-environments/)
    * [ Tutoriel - Guide utilisateur - Introduction  ](tutorial/)

Tutoriel - Guide utilisateur - Introduction

      * [ Démarrage  ](tutorial/first-steps/)
      * [ Paramètres de chemin  ](tutorial/path-params/)
      * [ Paramètres de requête  ](tutorial/query-params/)
      * [ Corps de la requête  ](tutorial/body/)
      * [ Paramètres de requête et validations de chaînes de caractères  ](tutorial/query-params-str-validations/)
      * [ Paramètres de chemin et validations numériques  ](tutorial/path-params-numeric-validations/)
      * [ Query Parameter Models  ](tutorial/query-param-models/)
      * [ Body - Paramètres multiples  ](tutorial/body-multiple-params/)
      * [ Body - Fields  ](tutorial/body-fields/)
      * [ Body - Nested Models  ](tutorial/body-nested-models/)
      * [ Declare Request Example Data  ](tutorial/schema-extra-example/)
      * [ Extra Data Types  ](tutorial/extra-data-types/)
      * [ Cookie Parameters  ](tutorial/cookie-params/)
      * [ Header Parameters  ](tutorial/header-params/)
      * [ Cookie Parameter Models  ](tutorial/cookie-param-models/)
      * [ Header Parameter Models  ](tutorial/header-param-models/)
      * [ Response Model - Return Type  ](tutorial/response-model/)
      * [ Extra Models  ](tutorial/extra-models/)
      * [ Response Status Code  ](tutorial/response-status-code/)
      * [ Form Data  ](tutorial/request-forms/)
      * [ Form Models  ](tutorial/request-form-models/)
      * [ Request Files  ](tutorial/request-files/)
      * [ Request Forms and Files  ](tutorial/request-forms-and-files/)
      * [ Handling Errors  ](tutorial/handling-errors/)
      * [ Path Operation Configuration  ](tutorial/path-operation-configuration/)
      * [ JSON Compatible Encoder  ](tutorial/encoder/)
      * [ Body - Updates  ](tutorial/body-updates/)
      * [ Dependencies  ](tutorial/dependencies/)

Dependencies

        * [ Classes as Dependencies  ](tutorial/dependencies/classes-as-dependencies/)
        * [ Sub-dependencies  ](tutorial/dependencies/sub-dependencies/)
        * [ Dependencies in path operation decorators  ](tutorial/dependencies/dependencies-in-path-operation-decorators/)
        * [ Global Dependencies  ](tutorial/dependencies/global-dependencies/)
        * [ Dependencies with yield  ](tutorial/dependencies/dependencies-with-yield/)
      * [ Security  ](tutorial/security/)

Security

        * [ Security - First Steps  ](tutorial/security/first-steps/)
        * [ Get Current User  ](tutorial/security/get-current-user/)
        * [ Simple OAuth2 with Password and Bearer  ](tutorial/security/simple-oauth2/)
        * [ OAuth2 with Password (and hashing), Bearer with JWT tokens  ](tutorial/security/oauth2-jwt/)
      * [ Middleware  ](tutorial/middleware/)
      * [ CORS (Cross-Origin Resource Sharing)  ](tutorial/cors/)
      * [ SQL (Relational) Databases  ](tutorial/sql-databases/)
      * [ Bigger Applications - Multiple Files  ](tutorial/bigger-applications/)
      * [ Tâches d'arrière-plan  ](tutorial/background-tasks/)
      * [ Metadata and Docs URLs  ](tutorial/metadata/)
      * [ Static Files  ](tutorial/static-files/)
      * [ Testing  ](tutorial/testing/)
      * [ Débogage ](tutorial/debugging/)
    * [ Guide de l'utilisateur avancé  ](advanced/)

Guide de l'utilisateur avancé

      * [ Configuration avancée des paramètres de chemin  ](advanced/path-operation-advanced-configuration/)
      * [ Codes HTTP supplémentaires  ](advanced/additional-status-codes/)
      * [ Renvoyer directement une réponse  ](advanced/response-directly/)
      * [ Custom Response - HTML, Stream, File, others  ](advanced/custom-response/)
      * [ Réponses supplémentaires dans OpenAPI  ](advanced/additional-responses/)
      * [ Response Cookies  ](advanced/response-cookies/)
      * [ Response Headers  ](advanced/response-headers/)
      * [ Response - Change Status Code  ](advanced/response-change-status-code/)
      * [ Advanced Dependencies  ](advanced/advanced-dependencies/)
      * [ Advanced Security  ](advanced/security/)

Advanced Security

        * [ OAuth2 scopes  ](advanced/security/oauth2-scopes/)
        * [ HTTP Basic Auth  ](advanced/security/http-basic-auth/)
      * [ Using the Request Directly  ](advanced/using-request-directly/)
      * [ Using Dataclasses  ](advanced/dataclasses/)
      * [ Advanced Middleware  ](advanced/middleware/)
      * [ Sub Applications - Mounts  ](advanced/sub-applications/)
      * [ Behind a Proxy  ](advanced/behind-a-proxy/)
      * [ Templates  ](advanced/templates/)
      * [ WebSockets  ](advanced/websockets/)
      * [ Lifespan Events  ](advanced/events/)
      * [ Testing WebSockets  ](advanced/testing-websockets/)
      * [ Testing Events: startup - shutdown  ](advanced/testing-events/)
      * [ Testing Dependencies with Overrides  ](advanced/testing-dependencies/)
      * [ Async Tests  ](advanced/async-tests/)
      * [ Settings and Environment Variables  ](advanced/settings/)
      * [ OpenAPI Callbacks  ](advanced/openapi-callbacks/)
      * [ OpenAPI Webhooks  ](advanced/openapi-webhooks/)
      * [ Including WSGI - Flask, Django, others  ](advanced/wsgi/)
      * [ Generate Clients  ](advanced/generate-clients/)
    * [ FastAPI CLI  ](fastapi-cli/)
    * [ Déploiement  ](deployment/)

Déploiement

      * [ À propos des versions de FastAPI  ](deployment/versions/)
      * [ À propos de HTTPS  ](deployment/https/)
      * [ Exécuter un serveur manuellement - Uvicorn  ](deployment/manually/)
      * [ Deployments Concepts  ](deployment/concepts/)
      * [ Deploy FastAPI on Cloud Providers  ](deployment/cloud/)
      * [ Server Workers - Uvicorn with Workers  ](deployment/server-workers/)
      * [ Déployer avec Docker  ](deployment/docker/)
    * [ How To - Recipes  ](how-to/)

How To - Recipes

      * [ General - How To - Recipes  ](how-to/general/)
      * [ GraphQL  ](how-to/graphql/)
      * [ Custom Request and APIRoute class  ](how-to/custom-request-and-route/)
      * [ Conditional OpenAPI  ](how-to/conditional-openapi/)
      * [ Extending OpenAPI  ](how-to/extending-openapi/)
      * [ Separate OpenAPI Schemas for Input and Output or Not  ](how-to/separate-openapi-schemas/)
      * [ Custom Docs UI Static Assets (Self-Hosting)  ](how-to/custom-docs-ui-assets/)
      * [ Configure Swagger UI  ](how-to/configure-swagger-ui/)
      * [ Testing a Database  ](how-to/testing-database/)
  * [ Reference  ](reference/)

Reference

    * [ `FastAPI` class  ](reference/fastapi/)
    * [ Request Parameters  ](reference/parameters/)
    * [ Status Codes  ](reference/status/)
    * [ `UploadFile` class  ](reference/uploadfile/)
    * [ Exceptions - `HTTPException` and `WebSocketException` ](reference/exceptions/)
    * [ Dependencies - `Depends()` and `Security()` ](reference/dependencies/)
    * [ `APIRouter` class  ](reference/apirouter/)
    * [ Background Tasks - `BackgroundTasks` ](reference/background/)
    * [ `Request` class  ](reference/request/)
    * [ WebSockets  ](reference/websockets/)
    * [ `HTTPConnection` class  ](reference/httpconnection/)
    * [ `Response` class  ](reference/response/)
    * [ Custom Response Classes - File, HTML, Redirect, Streaming, etc.  ](reference/responses/)
    * [ Middleware  ](reference/middleware/)
    * [ OpenAPI  ](reference/openapi/)

OpenAPI

      * [ OpenAPI `docs` ](reference/openapi/docs/)
      * [ OpenAPI `models` ](reference/openapi/models/)
    * [ Security Tools  ](reference/security/)
    * [ Encoders - `jsonable_encoder` ](reference/encoders/)
    * [ Static Files - `StaticFiles` ](reference/staticfiles/)
    * [ Templating - `Jinja2Templates` ](reference/templating/)
    * [ Test Client - `TestClient` ](reference/testclient/)
  * [ FastAPI People  ](fastapi-people/)
  * [ Resources  ](resources/)

Resources

    * [ Help FastAPI - Obtenir de l'aide  ](help-fastapi/)
    * [ Development - Contributing  ](contributing/)
    * [ Génération de projets - Modèle  ](project-generation/)
    * [ External Links and Articles  ](external-links/)
    * [ FastAPI and friends newsletter  ](newsletter/)
    * [ Repository Management Tasks  ](management-tasks/)
  * [ About  ](about/)

About

    * [ Alternatives, inspiration et comparaisons  ](alternatives/)
    * [ Histoire, conception et avenir  ](history-design-future/)
    * [ Test de performance  ](benchmarks/)
    * [ Repository Management  ](management/)
  * [ Release Notes  ](release-notes/)

Table des matières

  * Sponsors 
  * Opinions 
  * **Typer** , le FastAPI des CLI
  * Prérequis 
  * Installation 
  * Exemple 
    * Créez 
    * Lancez 
    * Vérifiez 
    * Documentation API interactive 
    * Documentation API alternative 
  * Exemple plus poussé 
    * Plus loin avec la documentation API interactive 
    * Plus loin avec la documentation API alternative 
    * En résumé 
  * Performance 
  * Dépendances facultatives 
  * Licence 

# FastAPI¶

[![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-
teal.png)](https://fastapi.tiangolo.com)

_Framework FastAPI, haute performance, facile à apprendre, rapide à coder,
prêt pour la production_

[
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master)
](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)
[ ![Coverage](https://coverage-
badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ](https://coverage-
badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi) [ ![Package
version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)
](https://pypi.org/project/fastapi) [ ![Supported Python
versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
](https://pypi.org/project/fastapi)

* * *

**Documentation** : <https://fastapi.tiangolo.com>

**Code Source** : <https://github.com/fastapi/fastapi>

* * *

FastAPI est un framework web moderne et rapide (haute performance) pour la
création d'API avec Python, basé sur les annotations de type standard de
Python.

Les principales fonctionnalités sont :

  * **Rapidité** : De très hautes performances, au niveau de **NodeJS** et **Go** (grâce à Starlette et Pydantic). L'un des frameworks Python les plus rapides.
  * **Rapide à coder** : Augmente la vitesse de développement des fonctionnalités d'environ 200 % à 300 %. *
  * **Moins de bugs** : Réduit d'environ 40 % les erreurs induites par le développeur. *
  * **Intuitif** : Excellente compatibilité avec les IDE. Complétion complète. Moins de temps passé à déboguer.
  * **Facile** : Conçu pour être facile à utiliser et à apprendre. Moins de temps passé à lire la documentation.
  * **Concis** : Diminue la duplication de code. De nombreuses fonctionnalités liées à la déclaration de chaque paramètre. Moins de bugs.
  * **Robuste** : Obtenez un code prêt pour la production. Avec une documentation interactive automatique.
  * **Basé sur des normes** : Basé sur (et entièrement compatible avec) les standards ouverts pour les APIs : [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (précédemment connu sous le nom de Swagger) et [JSON Schema](https://json-schema.org/).

* estimation basée sur des tests d'une équipe de développement interne, construisant des applications de production.

## Sponsors¶

[![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io?ref=fastapi
"BlockBee Cryptocurrency Payment Gateway")
[![](https://fastapi.tiangolo.com/img/sponsors/platform-
sh.png)](https://platform.sh/try-it-now/?utm_source=fastapi-
signup&utm_medium=banner&utm_campaign=FastAPI-signup-June-2023 "Build, run and
scale your apps on a modern, reliable, and secure PaaS.")
[![](https://fastapi.tiangolo.com/img/sponsors/porter.png)](https://www.porter.run
"Deploy FastAPI on AWS with a few clicks")
[![](https://fastapi.tiangolo.com/img/sponsors/bump-
sh.svg)](https://bump.sh/fastapi?utm_source=fastapi&utm_medium=referral&utm_campaign=sponsor
"Automate FastAPI documentation generation with Bump.sh")
[![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-
badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI
files")
[![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge
"Auth, user management and more for your B2B product")
[![](https://fastapi.tiangolo.com/img/sponsors/coherence.png)](https://www.withcoherence.com/?utm_medium=advertising&utm_source=fastapi&utm_campaign=website
"Coherence")
[![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png)](https://www.mongodb.com/developer/languages/python/python-
quickstart-
fastapi/?utm_campaign=fastapi_framework&utm_source=fastapi_sponsorship&utm_medium=web_referral
"Simplify Full Stack Development with FastAPI & MongoDB")
[![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-
gh "Zuplo: Scale, Protect, Document, and Monetize your FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com?utm_source=fastapi
"liblab - Generate SDKs from FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-
fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy
& scale any full-stack web app on Render. Focus on building apps, not infra.")
[![](https://fastapi.tiangolo.com/img/sponsors/haystack-
fastapi.svg)](https://github.com/deepset-ai/haystack/ "Build powerful search
from composable, open source building blocks")
[![](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/
"Pay as you go for market data")
[![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com?utm_source=fastapi+repo&utm_medium=github+sponsorship
"SDKs for your API | Speakeasy")
[![](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/
"Svix - Webhooks as a service")
[![](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral
"Stainless | Generate best-in-class SDKs")

[Other sponsors](https://fastapi.tiangolo.com/fastapi-people/#sponsors)

## Opinions¶

" _[...] J'utilise beaucoup **FastAPI** ces derniers temps. [...] Je prévois
de l'utiliser dans mon équipe pour tous les **services de ML chez Microsoft**.
Certains d'entre eux seront intégrés dans le coeur de **Windows** et dans
certains produits **Office**._"

Kabir Khan - **Microsoft** [(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

" _Nous avons adopté la bibliothèque **FastAPI** pour créer un serveur
**REST** qui peut être interrogé pour obtenir des **prédictions**. [pour
Ludwig]_"

Piero Molino, Yaroslav Dudin et Sai Sumanth Miryala - **Uber**
[(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

" _ **Netflix** a le plaisir d'annoncer la sortie en open-source de notre
framework d'orchestration de **gestion de crise** : **Dispatch** ! [construit
avec **FastAPI** ]_"

Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix**
[(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

" _Je suis très enthousiaste à propos de **FastAPI**. C'est un bonheur !_"

Brian Okken - **Auteur du podcast[Python
Bytes](https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-
wrongs?time_in_sec=855)**
[(ref)](https://twitter.com/brianokken/status/1112220079972728832)

* * *

" _Honnêtement, ce que vous avez construit a l'air super solide et élégant. A
bien des égards, c'est comme ça que je voulais que **Hug** soit - c'est
vraiment inspirant de voir quelqu'un construire ça._"

Timothy Crosley - **Créateur de[Hug](https://github.com/hugapi/hug)**
[(ref)](https://news.ycombinator.com/item?id=19455465)

* * *

" _Si vous cherchez à apprendre un **framework moderne** pour créer des APIs
REST, regardez **FastAPI** [...] C'est rapide, facile à utiliser et à
apprendre [...]_"

" _Nous sommes passés à **FastAPI** pour nos **APIs** [...] Je pense que vous
l'aimerez [...]_"

Ines Montani - Matthew Honnibal - **Fondateurs de[Explosion
AI](https://explosion.ai) \- Créateurs de [spaCy](https://spacy.io)**
[(ref)](https://twitter.com/_inesmontani/status/1144173225322143744) \-
[(ref)](https://twitter.com/honnibal/status/1144031421859655680)

* * *

" _Si quelqu'un cherche à construire une API Python de production, je
recommande vivement **FastAPI**. Il est **bien conçu** , **simple à utiliser**
et **très évolutif**. Il est devenu un **composant clé** dans notre stratégie
de développement API first et il est à l'origine de nombreux automatismes et
services tels que notre ingénieur virtuel TAC._"

Deon Pillsbury - **Cisco**
[(ref)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-
activity-6963242628536487936-trAp/)

* * *

## **Typer** , le FastAPI des CLI¶

[![](https://typer.tiangolo.com/img/logo-margin/logo-margin-
vector.svg)](https://typer.tiangolo.com)

Si vous souhaitez construire une application CLI utilisable dans un terminal
au lieu d'une API web, regardez [**Typer**](https://typer.tiangolo.com/).

**Typer** est le petit frère de FastAPI. Et il est destiné à être le **FastAPI
des CLI**. ⌨️ 🚀

## Prérequis¶

FastAPI repose sur les épaules de géants :

  * [Starlette](https://www.starlette.io/) pour les parties web.
  * [Pydantic](https://docs.pydantic.dev/) pour les parties données.

## Installation¶

    
    
    $ pip install fastapi
    
    ---> 100%
    

Vous aurez également besoin d'un serveur ASGI pour la production tel que
[Uvicorn](https://www.uvicorn.org) ou
[Hypercorn](https://github.com/pgjones/hypercorn).

    
    
    $ pip install "uvicorn[standard]"
    
    ---> 100%
    

## Exemple¶

### Créez¶

  * Créez un fichier `main.py` avec :

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

Ou utilisez `async def` ...

Si votre code utilise `async` / `await`, utilisez `async def` :

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    async def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

**Note**

Si vous n'êtes pas familier avec cette notion, consultez la section _"Vous
êtes pressés ?"_ à propos de [`async` et `await` dans la
documentation](https://fastapi.tiangolo.com/fr/async/#vous-etes-presses).

### Lancez¶

Lancez le serveur avec :

    
    
    $ uvicorn main:app --reload
    
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [28720]
    INFO:     Started server process [28722]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    

À propos de la commande `uvicorn main:app --reload` ...

La commande `uvicorn main:app` fait référence à :

  * `main` : le fichier `main.py` (le "module" Python).
  * `app` : l'objet créé à l'intérieur de `main.py` avec la ligne `app = FastAPI()`.
  * `--reload` : fait redémarrer le serveur après des changements de code. À n'utiliser que pour le développement.

### Vérifiez¶

Ouvrez votre navigateur à l'adresse
<http://127.0.0.1:8000/items/5?q=somequery>.

Vous obtenez alors cette réponse JSON :

    
    
    {"item_id": 5, "q": "somequery"}
    

Vous venez de créer une API qui :

  * Reçoit les requêtes HTTP pour les _chemins_ `/` et `/items/{item_id}`.
  * Les deux _chemins_ acceptent des _opérations_ `GET` (également connu sous le nom de _méthodes_ HTTP).
  * Le _chemin_ `/items/{item_id}` a un _paramètre_ `item_id` qui doit être un `int`.
  * Le _chemin_ `/items/{item_id}` a un _paramètre de requête_ optionnel `q` de type `str`.

### Documentation API interactive¶

Maintenant, rendez-vous sur <http://127.0.0.1:8000/docs>.

Vous verrez la documentation interactive automatique de l'API (fournie par
[Swagger UI](https://github.com/swagger-api/swagger-ui)) :

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-
simple.png)

### Documentation API alternative¶

Et maintenant, rendez-vous sur <http://127.0.0.1:8000/redoc>.

Vous verrez la documentation interactive automatique de l'API (fournie par
[ReDoc](https://github.com/Rebilly/ReDoc)) :

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## Exemple plus poussé¶

Maintenant, modifiez le fichier `main.py` pour recevoir le corps d'une requête
`PUT`.

Déclarez ce corps en utilisant les types Python standards, grâce à Pydantic.

    
    
    from typing import Union
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        price: float
        is_offer: Union[bool, None] = None
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    
    
    @app.put("/items/{item_id}")
    def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}
    

Le serveur se recharge normalement automatiquement (car vous avez pensé à
`--reload` dans la commande `uvicorn` ci-dessus).

### Plus loin avec la documentation API interactive¶

Maintenant, rendez-vous sur <http://127.0.0.1:8000/docs>.

  * La documentation interactive de l'API sera automatiquement mise à jour, y compris le nouveau corps de la requête :

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

  * Cliquez sur le bouton "Try it out", il vous permet de renseigner les paramètres et d'interagir directement avec l'API :

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

  * Cliquez ensuite sur le bouton "Execute", l'interface utilisateur communiquera avec votre API, enverra les paramètres, obtiendra les résultats et les affichera à l'écran :

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### Plus loin avec la documentation API alternative¶

Et maintenant, rendez-vous sur <http://127.0.0.1:8000/redoc>.

  * La documentation alternative reflétera également le nouveau paramètre de requête et le nouveau corps :

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### En résumé¶

En résumé, vous déclarez **une fois** les types de paramètres, le corps de la
requête, etc. en tant que paramètres de fonction.

Vous faites cela avec les types Python standard modernes.

Vous n'avez pas à apprendre une nouvelle syntaxe, les méthodes ou les classes
d'une bibliothèque spécifique, etc.

Juste du **Python** standard.

Par exemple, pour un `int`:

    
    
    item_id: int
    

ou pour un modèle `Item` plus complexe :

    
    
    item: Item
    

... et avec cette déclaration unique, vous obtenez :

  * Une assistance dans votre IDE, notamment :
    * la complétion.
    * la vérification des types.
  * La validation des données :
    * des erreurs automatiques et claires lorsque les données ne sont pas valides.
    * une validation même pour les objets JSON profondément imbriqués.
  * Une conversion des données d'entrée : venant du réseau et allant vers les données et types de Python, permettant de lire :
    * le JSON.
    * les paramètres du chemin.
    * les paramètres de la requête.
    * les cookies.
    * les en-têtes.
    * les formulaires.
    * les fichiers.
  * La conversion des données de sortie : conversion des données et types Python en données réseau (au format JSON), permettant de convertir :
    * les types Python (`str`, `int`, `float`, `bool`, `list`, etc).
    * les objets `datetime`.
    * les objets `UUID`.
    * les modèles de base de données.
    * ... et beaucoup plus.
  * La documentation API interactive automatique, avec 2 interfaces utilisateur au choix :
    * Swagger UI.
    * ReDoc.

* * *

Pour revenir à l'exemple de code précédent, **FastAPI** permet de :

  * Valider que `item_id` existe dans le chemin des requêtes `GET` et `PUT`.
  * Valider que `item_id` est de type `int` pour les requêtes `GET` et `PUT`.
    * Si ce n'est pas le cas, le client voit une erreur utile et claire.
  * Vérifier qu'il existe un paramètre de requête facultatif nommé `q` (comme dans `http://127.0.0.1:8000/items/foo?q=somequery`) pour les requêtes `GET`.
    * Puisque le paramètre `q` est déclaré avec `= None`, il est facultatif.
    * Sans le `None`, il serait nécessaire (comme l'est le corps de la requête dans le cas du `PUT`).
  * Pour les requêtes `PUT` vers `/items/{item_id}`, de lire le corps en JSON :
    * Vérifier qu'il a un attribut obligatoire `name` qui devrait être un `str`.
    * Vérifier qu'il a un attribut obligatoire `prix` qui doit être un `float`.
    * Vérifier qu'il a un attribut facultatif `is_offer`, qui devrait être un `bool`, s'il est présent.
    * Tout cela fonctionnerait également pour les objets JSON profondément imbriqués.
  * Convertir de et vers JSON automatiquement.
  * Documenter tout avec OpenAPI, qui peut être utilisé par :
    * Les systèmes de documentation interactifs.
    * Les systèmes de génération automatique de code client, pour de nombreuses langues.
  * Fournir directement 2 interfaces web de documentation interactive.

* * *

Nous n'avons fait qu'effleurer la surface, mais vous avez déjà une idée de la
façon dont tout cela fonctionne.

Essayez de changer la ligne contenant :

    
    
        return {"item_name": item.name, "item_id": item_id}
    

... de :

    
    
            ... "item_name": item.name ...
    

... vers :

    
    
            ... "item_price": item.price ...
    

... et voyez comment votre éditeur complétera automatiquement les attributs et
connaîtra leurs types :

![compatibilité IDE](https://fastapi.tiangolo.com/img/vscode-completion.png)

Pour un exemple plus complet comprenant plus de fonctionnalités, voir le
[Tutoriel - Guide utilisateur](https://fastapi.tiangolo.com/fr/tutorial/).

**Spoiler alert** : le tutoriel - guide utilisateur inclut :

  * Déclaration de **paramètres** provenant d'autres endroits différents comme : **en-têtes.**, **cookies** , **champs de formulaire** et **fichiers**.
  * L'utilisation de **contraintes de validation** comme `maximum_length` ou `regex`.
  * Un **système d'injection de dépendance** très puissant et facile à utiliser .
  * Sécurité et authentification, y compris la prise en charge de **OAuth2** avec les **jetons JWT** et l'authentification **HTTP Basic**.
  * Des techniques plus avancées (mais tout aussi faciles) pour déclarer les **modèles JSON profondément imbriqués** (grâce à Pydantic).
  * Intégration de **GraphQL** avec [Strawberry](https://strawberry.rocks) et d'autres bibliothèques.
  * D'obtenir de nombreuses fonctionnalités supplémentaires (grâce à Starlette) comme :
    * **WebSockets**
    * de tester le code très facilement avec `requests` et `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ... et plus encore.

## Performance¶

Les benchmarks TechEmpower indépendants montrent que les applications
**FastAPI** s'exécutant sous Uvicorn sont [ parmi les frameworks existants en
Python les plus rapides
](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7),
juste derrière Starlette et Uvicorn (utilisés en interne par FastAPI). (*)

Pour en savoir plus, consultez la section
[Benchmarks](https://fastapi.tiangolo.com/fr/benchmarks/).

## Dépendances facultatives¶

Utilisées par Pydantic:

  * [`email-validator`](https://github.com/JoshData/python-email-validator) \- pour la validation des adresses email.

Utilisées par Starlette :

  * [`requests`](https://requests.readthedocs.io) \- Obligatoire si vous souhaitez utiliser `TestClient`.
  * [`jinja2`](https://jinja.palletsprojects.com) \- Obligatoire si vous souhaitez utiliser la configuration de template par défaut.
  * [`python-multipart`](https://github.com/Kludex/python-multipart) \- Obligatoire si vous souhaitez supporter le "décodage" de formulaire avec `request.form()`.
  * [`itsdangerous`](https://pythonhosted.org/itsdangerous/) \- Obligatoire pour la prise en charge de `SessionMiddleware`.
  * [`pyyaml`](https://pyyaml.org/wiki/PyYAMLDocumentation) \- Obligatoire pour le support `SchemaGenerator` de Starlette (vous n'en avez probablement pas besoin avec FastAPI).

Utilisées par FastAPI / Starlette :

  * [`uvicorn`](https://www.uvicorn.org) \- Pour le serveur qui charge et sert votre application.
  * [`orjson`](https://github.com/ijl/orjson) \- Obligatoire si vous voulez utiliser `ORJSONResponse`.
  * [`ujson`](https://github.com/esnme/ultrajson) \- Obligatoire si vous souhaitez utiliser `UJSONResponse`.

Vous pouvez tout installer avec `pip install fastapi[all]`.

## Licence¶

Ce projet est soumis aux termes de la licence MIT.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!

Retour en haut de la page

  *[Completion]: also known as auto-complete, autocompletion, IntelliSense
  *[CLI]: Command Line Interface
  *[Conversion]: also known as: serialization, parsing, marshalling
  *[Dependency Injection]: also known as components, resources, providers, services, injectables
  *["parsing"]: convertir el string que viene de un request HTTP en datos de Python
  *[tip məsləhətlərinə]: Tip Məsləhətləri: Type Hints
  *[otomatik tamamlama]: auto-complete, autocompletion, IntelliSense olaraq da bilinir
  *[_yollarında_]: Yol: Path 
  *[gövdə]: Gövdə: Body 
  *[çevirmək]: Çevrilmə: serialization, parsing, marshalling olaraq da bilinir
  *[Yol]: Yol: Path
  *[Sorğu]: Sorğu: Query
  *[Çərəzlər]: Çərəz: Cookie
  *[Başlıqlaq]: Başlıq: Header
  *[Formalar]: Forma: Form
  *[yolda]: Yol: Path
  *[məcburi olmayan]: Məcburi olmayan: Optional
  *[müştəri]: Müştəri: Client
  *[**başlıqlar**]: Başlıq: Header
  *[çərəzlər]: Çərəz: Cookie
  *[Müqayisələr]: Müqayisələr: Benchmarks
  *[şablon]: Şablon: Template
  *["çevirmə"]: HTTP sorğusu ilə alınan string məlumatın Python obyektinə çevrilməsi
  *[টাইপ্স]: একটি ভেরিয়েবল কি ধরনের ডেটা ধারণ করতে পারে।
  *[রূপান্তর]: যা পরিচিত: serialization, parsing, marshalling
  *[ডিপেন্ডেন্সি ইনজেকশন]: also known as components, resources, providers, services, injectables
  *[Code-Vervollständigung]: auch bekannt als Autovervollständigung, Autocompletion, IntelliSense
  *[ASGI]: Asynchronous Server Gateway Interface – Asynchrone Server-Verbindungsschnittstelle
  *[Body]: Body – Körper, Inhalt: Der eigentliche Inhalt einer Nachricht, nicht die Metadaten
  *[Konvertierung]: auch bekannt als: Serialisierung, Parsen, Marshalling
  *[„parsen“]: Konvertieren des Strings, der aus einer HTTP-Anfrage stammt, nach Python-Daten
  *[Autocompletado]: también conocido como autocompletado, IntelliSense
  *[Conversión]: también conocido como: serialización, parsing, marshalling
  *[Inyección de Dependencias]: también conocido como componentes, recursos, proveedores, servicios, inyectables
  *[واسط خط فرمان]: CLI (Command Line Interface)
  *[سرعت]: Fast
  *[کدنویسی سریع]: Fast to code
  *[باگ کمتر]: Fewer bugs
  *[هوشمندانه]: Intuitive
  *[تکمیل]: یا اتوکامپلیت، اتوکامپلشن، اینتلیسنس
  *[آسان]: Easy
  *[کوچک]: Short
  *[استوار]: Robust
  *[مستندات تعاملی]: Interactive documentation
  *[مبتنی بر استانداردها]: Standards-based
  *[عملیات]: operations در OpenAPI
  *[_پارامتر مسیر_]: Path Parameter
  *[_پارامتر پرسمان_]: Query Parameter
  *[بدنه]: Body
  *[انواع]: Type
  *[نحو]: Syntax
  *[تبدیل]: serialization, parsing, marshalling
  *[پارامترهای مسیر]: Path parameters
  *[پارامترهای پرسمان]: Query parameters
  *[کوکی‌ها]: Cookies
  *[سرآیند‌ها (هدرها)]: Headers
  *[فرم‌ها]: Forms
  *[فایل‌ها]: Files
  *[محدودیت‌های اعتبارسنجی]: Validation Constraints
  *[وب‌سوکت]: WebSocket
  *["تجزیه (parse)"]: تبدیل رشته متنی موجود در درخواست HTTP به انواع داده پایتون
  *[Débogage]: En anglais: Debugging
  *[Complétion]: également connu sous le nom d'auto-complétion, autocomplétion, IntelliSense
  *[ CLI]: Command Line Interface
  *[JSON]: JavaScript Object Notation
  *[paramètre]: en anglais : path parameter
  *[paramètre de requête]: en anglais : query param
  *[le corps]: en anglais : body
  *[Une conversion]: aussi connu sous le nom de : serialization, parsing, marshalling
  *[les paramètres du chemin]: en anglais : path parameters
  *[les paramètres de la requête]: en anglais : query parameters
  *[les en-têtes]: en anglais : headers
  *[les formulaires]: en anglais : forms
  *[les fichiers]: en anglais : files
  *[La conversion]: aussi connu sous le nom de : serialization, parsing, marshalling
  *[en-têtes]: en anglais : headers
  *[système d'injection de dépendance]: aussi connu sous le nom de composants, ressources, fournisseurs, services, injectables
  *[ JWT]: JSON Web Tokens
  *[ JSON]: JavaScript Object Notation
  *[CORS]: Cross-Origin Resource Sharing
  *["décodage"]: convertit la chaine de caractère d'une requête HTTP en donnée Python



---

# https://fastapi.tiangolo.com/he/



[ ![logo](img/icon-white.svg) ](. "FastAPI") FastAPI

[ fastapi/fastapi  ](https://github.com/fastapi/fastapi "לעבור אל המאגר")

  * FastAPI  [ FastAPI  ](.) תוכן העניינים 
    * נותני חסות 
    * דעות 
    * **Typer** , ה - FastAPI של ממשקי שורת פקודה (CLI). 
    * תלויות 
    * התקנה 
    * דוגמא 
      * צרו אותה 
      * הריצו אותה 
      * בדקו אותה 
      * תיעוד API אינטרקטיבי 
      * תיעוד אלטרנטיבי 
    * שדרוג לדוגמא 
      * שדרוג התיעוד האינטרקטיבי 
      * שדרוג התיעוד האלטרנטיבי 
      * סיכום 
    * ביצועים 
    * תלויות אופציונליות 
    * רשיון 
  * [ Features  ](features/)
  * [ Learn  ](learn/)

Learn

    * [ Python Types Intro  ](python-types/)
    * [ Concurrency and async / await  ](async/)
    * [ Environment Variables  ](environment-variables/)
    * [ Virtual Environments  ](virtual-environments/)
    * [ Tutorial - User Guide  ](tutorial/)

Tutorial - User Guide

      * [ First Steps  ](tutorial/first-steps/)
      * [ Path Parameters  ](tutorial/path-params/)
      * [ Query Parameters  ](tutorial/query-params/)
      * [ Request Body  ](tutorial/body/)
      * [ Query Parameters and String Validations  ](tutorial/query-params-str-validations/)
      * [ Path Parameters and Numeric Validations  ](tutorial/path-params-numeric-validations/)
      * [ Query Parameter Models  ](tutorial/query-param-models/)
      * [ Body - Multiple Parameters  ](tutorial/body-multiple-params/)
      * [ Body - Fields  ](tutorial/body-fields/)
      * [ Body - Nested Models  ](tutorial/body-nested-models/)
      * [ Declare Request Example Data  ](tutorial/schema-extra-example/)
      * [ Extra Data Types  ](tutorial/extra-data-types/)
      * [ Cookie Parameters  ](tutorial/cookie-params/)
      * [ Header Parameters  ](tutorial/header-params/)
      * [ Cookie Parameter Models  ](tutorial/cookie-param-models/)
      * [ Header Parameter Models  ](tutorial/header-param-models/)
      * [ Response Model - Return Type  ](tutorial/response-model/)
      * [ Extra Models  ](tutorial/extra-models/)
      * [ Response Status Code  ](tutorial/response-status-code/)
      * [ Form Data  ](tutorial/request-forms/)
      * [ Form Models  ](tutorial/request-form-models/)
      * [ Request Files  ](tutorial/request-files/)
      * [ Request Forms and Files  ](tutorial/request-forms-and-files/)
      * [ Handling Errors  ](tutorial/handling-errors/)
      * [ Path Operation Configuration  ](tutorial/path-operation-configuration/)
      * [ JSON Compatible Encoder  ](tutorial/encoder/)
      * [ Body - Updates  ](tutorial/body-updates/)
      * [ Dependencies  ](tutorial/dependencies/)

Dependencies

        * [ Classes as Dependencies  ](tutorial/dependencies/classes-as-dependencies/)
        * [ Sub-dependencies  ](tutorial/dependencies/sub-dependencies/)
        * [ Dependencies in path operation decorators  ](tutorial/dependencies/dependencies-in-path-operation-decorators/)
        * [ Global Dependencies  ](tutorial/dependencies/global-dependencies/)
        * [ Dependencies with yield  ](tutorial/dependencies/dependencies-with-yield/)
      * [ Security  ](tutorial/security/)

Security

        * [ Security - First Steps  ](tutorial/security/first-steps/)
        * [ Get Current User  ](tutorial/security/get-current-user/)
        * [ Simple OAuth2 with Password and Bearer  ](tutorial/security/simple-oauth2/)
        * [ OAuth2 with Password (and hashing), Bearer with JWT tokens  ](tutorial/security/oauth2-jwt/)
      * [ Middleware  ](tutorial/middleware/)
      * [ CORS (Cross-Origin Resource Sharing)  ](tutorial/cors/)
      * [ SQL (Relational) Databases  ](tutorial/sql-databases/)
      * [ Bigger Applications - Multiple Files  ](tutorial/bigger-applications/)
      * [ Background Tasks  ](tutorial/background-tasks/)
      * [ Metadata and Docs URLs  ](tutorial/metadata/)
      * [ Static Files  ](tutorial/static-files/)
      * [ Testing  ](tutorial/testing/)
      * [ Debugging  ](tutorial/debugging/)
    * [ Advanced User Guide  ](advanced/)

Advanced User Guide

      * [ Path Operation Advanced Configuration  ](advanced/path-operation-advanced-configuration/)
      * [ Additional Status Codes  ](advanced/additional-status-codes/)
      * [ Return a Response Directly  ](advanced/response-directly/)
      * [ Custom Response - HTML, Stream, File, others  ](advanced/custom-response/)
      * [ Additional Responses in OpenAPI  ](advanced/additional-responses/)
      * [ Response Cookies  ](advanced/response-cookies/)
      * [ Response Headers  ](advanced/response-headers/)
      * [ Response - Change Status Code  ](advanced/response-change-status-code/)
      * [ Advanced Dependencies  ](advanced/advanced-dependencies/)
      * [ Advanced Security  ](advanced/security/)

Advanced Security

        * [ OAuth2 scopes  ](advanced/security/oauth2-scopes/)
        * [ HTTP Basic Auth  ](advanced/security/http-basic-auth/)
      * [ Using the Request Directly  ](advanced/using-request-directly/)
      * [ Using Dataclasses  ](advanced/dataclasses/)
      * [ Advanced Middleware  ](advanced/middleware/)
      * [ Sub Applications - Mounts  ](advanced/sub-applications/)
      * [ Behind a Proxy  ](advanced/behind-a-proxy/)
      * [ Templates  ](advanced/templates/)
      * [ WebSockets  ](advanced/websockets/)
      * [ Lifespan Events  ](advanced/events/)
      * [ Testing WebSockets  ](advanced/testing-websockets/)
      * [ Testing Events: startup - shutdown  ](advanced/testing-events/)
      * [ Testing Dependencies with Overrides  ](advanced/testing-dependencies/)
      * [ Async Tests  ](advanced/async-tests/)
      * [ Settings and Environment Variables  ](advanced/settings/)
      * [ OpenAPI Callbacks  ](advanced/openapi-callbacks/)
      * [ OpenAPI Webhooks  ](advanced/openapi-webhooks/)
      * [ Including WSGI - Flask, Django, others  ](advanced/wsgi/)
      * [ Generate Clients  ](advanced/generate-clients/)
    * [ FastAPI CLI  ](fastapi-cli/)
    * [ Deployment  ](deployment/)

Deployment

      * [ About FastAPI versions  ](deployment/versions/)
      * [ About HTTPS  ](deployment/https/)
      * [ Run a Server Manually  ](deployment/manually/)
      * [ Deployments Concepts  ](deployment/concepts/)
      * [ Deploy FastAPI on Cloud Providers  ](deployment/cloud/)
      * [ Server Workers - Uvicorn with Workers  ](deployment/server-workers/)
      * [ FastAPI in Containers - Docker  ](deployment/docker/)
    * [ How To - Recipes  ](how-to/)

How To - Recipes

      * [ General - How To - Recipes  ](how-to/general/)
      * [ GraphQL  ](how-to/graphql/)
      * [ Custom Request and APIRoute class  ](how-to/custom-request-and-route/)
      * [ Conditional OpenAPI  ](how-to/conditional-openapi/)
      * [ Extending OpenAPI  ](how-to/extending-openapi/)
      * [ Separate OpenAPI Schemas for Input and Output or Not  ](how-to/separate-openapi-schemas/)
      * [ Custom Docs UI Static Assets (Self-Hosting)  ](how-to/custom-docs-ui-assets/)
      * [ Configure Swagger UI  ](how-to/configure-swagger-ui/)
      * [ Testing a Database  ](how-to/testing-database/)
  * [ Reference  ](reference/)

Reference

    * [ `FastAPI` class  ](reference/fastapi/)
    * [ Request Parameters  ](reference/parameters/)
    * [ Status Codes  ](reference/status/)
    * [ `UploadFile` class  ](reference/uploadfile/)
    * [ Exceptions - `HTTPException` and `WebSocketException` ](reference/exceptions/)
    * [ Dependencies - `Depends()` and `Security()` ](reference/dependencies/)
    * [ `APIRouter` class  ](reference/apirouter/)
    * [ Background Tasks - `BackgroundTasks` ](reference/background/)
    * [ `Request` class  ](reference/request/)
    * [ WebSockets  ](reference/websockets/)
    * [ `HTTPConnection` class  ](reference/httpconnection/)
    * [ `Response` class  ](reference/response/)
    * [ Custom Response Classes - File, HTML, Redirect, Streaming, etc.  ](reference/responses/)
    * [ Middleware  ](reference/middleware/)
    * [ OpenAPI  ](reference/openapi/)

OpenAPI

      * [ OpenAPI `docs` ](reference/openapi/docs/)
      * [ OpenAPI `models` ](reference/openapi/models/)
    * [ Security Tools  ](reference/security/)
    * [ Encoders - `jsonable_encoder` ](reference/encoders/)
    * [ Static Files - `StaticFiles` ](reference/staticfiles/)
    * [ Templating - `Jinja2Templates` ](reference/templating/)
    * [ Test Client - `TestClient` ](reference/testclient/)
  * [ FastAPI People  ](fastapi-people/)
  * [ Resources  ](resources/)

Resources

    * [ Help FastAPI - Get Help  ](help-fastapi/)
    * [ Development - Contributing  ](contributing/)
    * [ Full Stack FastAPI Template  ](project-generation/)
    * [ External Links and Articles  ](external-links/)
    * [ FastAPI and friends newsletter  ](newsletter/)
    * [ Repository Management Tasks  ](management-tasks/)
  * [ About  ](about/)

About

    * [ Alternatives, Inspiration and Comparisons  ](alternatives/)
    * [ History, Design and Future  ](history-design-future/)
    * [ Benchmarks  ](benchmarks/)
    * [ Repository Management  ](management/)
  * [ Release Notes  ](release-notes/)

תוכן העניינים

  * נותני חסות 
  * דעות 
  * **Typer** , ה - FastAPI של ממשקי שורת פקודה (CLI). 
  * תלויות 
  * התקנה 
  * דוגמא 
    * צרו אותה 
    * הריצו אותה 
    * בדקו אותה 
    * תיעוד API אינטרקטיבי 
    * תיעוד אלטרנטיבי 
  * שדרוג לדוגמא 
    * שדרוג התיעוד האינטרקטיבי 
    * שדרוג התיעוד האלטרנטיבי 
    * סיכום 
  * ביצועים 
  * תלויות אופציונליות 
  * רשיון 

# FastAPI¶

[![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-
teal.png)](https://fastapi.tiangolo.com)

_תשתית FastAPI, ביצועים גבוהים, קלה ללמידה, מהירה לתכנות, מוכנה לסביבת ייצור_

[
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master)
](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)
[
![Coverage](https://img.shields.io/codecov/c/github/fastapi/fastapi?color=%2334D058)
](https://codecov.io/gh/fastapi/fastapi) [ ![Package
version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)
](https://pypi.org/project/fastapi) [ ![Supported Python
versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
](https://pypi.org/project/fastapi)

* * *

**תיעוד** : <https://fastapi.tiangolo.com>

**קוד** : <https://github.com/fastapi/fastapi>

* * *

FastAPI היא תשתית רשת מודרנית ומהירה (ביצועים גבוהים) לבניית ממשקי תכנות
יישומים (API) עם פייתון 3.6+ בהתבסס על רמזי טיפוסים סטנדרטיים.

תכונות המפתח הן:

  * **מהירה** : ביצועים גבוהים מאוד, בקנה אחד עם NodeJS ו - Go (תודות ל - Starlette ו - Pydantic). אחת מתשתיות הפייתון המהירות ביותר.

  * **מהירה לתכנות** : הגבירו את מהירות פיתוח התכונות החדשות בכ - %200 עד %300. *

  * **פחות שגיאות** : מנעו כ - %40 משגיאות אנוש (מפתחים). *
  * **אינטואיטיבית** : תמיכת עורך מעולה. השלמה בכל מקום. פחות זמן ניפוי שגיאות.
  * **קלה** : מתוכננת להיות קלה לשימוש וללמידה. פחות זמן קריאת תיעוד.
  * **קצרה** : מזערו שכפול קוד. מספר תכונות מכל הכרזת פרמטר. פחות שגיאות.
  * **חסונה** : קבלו קוד מוכן לסביבת ייצור. עם תיעוד אינטרקטיבי אוטומטי.
  * **מבוססת סטנדרטים** : מבוססת על (ותואמת לחלוטין ל -) הסטדנרטים הפתוחים לממשקי תכנות יישומים: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (ידועים לשעבר כ - Swagger) ו - [JSON Schema](https://json-schema.org/).

* הערכה מבוססת על בדיקות של צוות פיתוח פנימי שבונה אפליקציות בסביבת ייצור.

## נותני חסות¶

[![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io?ref=fastapi
"BlockBee Cryptocurrency Payment Gateway")
[![](https://fastapi.tiangolo.com/img/sponsors/platform-
sh.png)](https://platform.sh/try-it-now/?utm_source=fastapi-
signup&utm_medium=banner&utm_campaign=FastAPI-signup-June-2023 "Build, run and
scale your apps on a modern, reliable, and secure PaaS.")
[![](https://fastapi.tiangolo.com/img/sponsors/porter.png)](https://www.porter.run
"Deploy FastAPI on AWS with a few clicks")
[![](https://fastapi.tiangolo.com/img/sponsors/bump-
sh.svg)](https://bump.sh/fastapi?utm_source=fastapi&utm_medium=referral&utm_campaign=sponsor
"Automate FastAPI documentation generation with Bump.sh")
[![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-
badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI
files")
[![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge
"Auth, user management and more for your B2B product")
[![](https://fastapi.tiangolo.com/img/sponsors/coherence.png)](https://www.withcoherence.com/?utm_medium=advertising&utm_source=fastapi&utm_campaign=website
"Coherence")
[![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png)](https://www.mongodb.com/developer/languages/python/python-
quickstart-
fastapi/?utm_campaign=fastapi_framework&utm_source=fastapi_sponsorship&utm_medium=web_referral
"Simplify Full Stack Development with FastAPI & MongoDB")
[![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-
gh "Zuplo: Scale, Protect, Document, and Monetize your FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com?utm_source=fastapi
"liblab - Generate SDKs from FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-
fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy
& scale any full-stack web app on Render. Focus on building apps, not infra.")
[![](https://fastapi.tiangolo.com/img/sponsors/haystack-
fastapi.svg)](https://github.com/deepset-ai/haystack/ "Build powerful search
from composable, open source building blocks")
[![](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/
"Pay as you go for market data")
[![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com?utm_source=fastapi+repo&utm_medium=github+sponsorship
"SDKs for your API | Speakeasy")
[![](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/
"Svix - Webhooks as a service")
[![](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral
"Stainless | Generate best-in-class SDKs")

[נותני חסות אחרים](https://fastapi.tiangolo.com/fastapi-people/#sponsors)

## דעות¶

" _[...] I'm using **FastAPI** a ton these days. [...] I'm actually planning
to use it for all of my team's **ML services at Microsoft**. Some of them are
getting integrated into the core **Windows** product and some **Office**
products._"

Kabir Khan - **Microsoft** [(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

" _We adopted the **FastAPI** library to spawn a **REST** server that can be
queried to obtain **predictions**. [for Ludwig]_"

Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - **Uber**
[(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

" _ **Netflix** is pleased to announce the open-source release of our **crisis
management** orchestration framework: **Dispatch**! [built with **FastAPI**
]_"

Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix**
[(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

" _I’m over the moon excited about **FastAPI**. It’s so fun!_"

Brian Okken - **[Python Bytes](https://pythonbytes.fm/episodes/show/123/time-
to-right-the-py-wrongs?time_in_sec=855) podcast host**
[(ref)](https://twitter.com/brianokken/status/1112220079972728832)

* * *

" _Honestly, what you've built looks super solid and polished. In many ways,
it's what I wanted **Hug** to be - it's really inspiring to see someone build
that._"

Timothy Crosley - **[Hug](https://github.com/hugapi/hug) creator**
[(ref)](https://news.ycombinator.com/item?id=19455465)

* * *

" _If you're looking to learn one **modern framework** for building REST APIs,
check out **FastAPI** [...] It's fast, easy to use and easy to learn [...]_"

" _We've switched over to **FastAPI** for our **APIs** [...] I think you'll
like it [...]_"

Ines Montani - Matthew Honnibal - **[Explosion AI](https://explosion.ai)
founders - [spaCy](https://spacy.io) creators**
[(ref)](https://twitter.com/_inesmontani/status/1144173225322143744) \-
[(ref)](https://twitter.com/honnibal/status/1144031421859655680)

* * *

## **Typer** , ה - FastAPI של ממשקי שורת פקודה (CLI).¶

[![](https://typer.tiangolo.com/img/logo-margin/logo-margin-
vector.svg)](https://typer.tiangolo.com)

אם אתם בונים אפליקציית CLI לשימוש במסוף במקום ממשק רשת, העיפו מבט על
[**Typer**](https://typer.tiangolo.com/).

**Typer** היא אחותה הקטנה של FastAPI. ומטרתה היא להיות ה - **FastAPI של ממשקי
שורת פקודה**. ⌨️ 🚀

## תלויות¶

פייתון 3.6+

FastAPI עומדת על כתפי ענקיות:

  * [Starlette](https://www.starlette.io/) לחלקי הרשת.
  * [Pydantic](https://docs.pydantic.dev/) לחלקי המידע.

## התקנה¶

    
    
    $ pip install fastapi
    
    ---> 100%
    

תצטרכו גם שרת ASGI כגון [Uvicorn](https://www.uvicorn.org) או
[Hypercorn](https://github.com/pgjones/hypercorn).

    
    
    $ pip install "uvicorn[standard]"
    
    ---> 100%
    

## דוגמא¶

### צרו אותה¶

  * צרו קובץ בשם `main.py` עם:

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

או השתמשו ב - `async def`...

אם הקוד שלכם משתמש ב - `async` / `await`, השתמשו ב - `async def`:

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    async def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

**שימו לב** :

אם אינכם יודעים, בדקו את פרק "ממהרים?" על [`async` ו - `await`
בתיעוד](https://fastapi.tiangolo.com/async/#in-a-hurry).

### הריצו אותה¶

התחילו את השרת עם:

    
    
    $ uvicorn main:app --reload
    
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [28720]
    INFO:     Started server process [28722]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    

על הפקודה `uvicorn main:app --reload`...

הפקודה `uvicorn main:app` מתייחסת ל:

  * `main`: הקובץ `main.py` (מודול פייתון).
  * `app`: האובייקט שנוצר בתוך `main.py` עם השורה `app = FastAPI()`.
  * `--reload`: גרמו לשרת להתאתחל לאחר שינויים בקוד. עשו זאת רק בסביבת פיתוח.

### בדקו אותה¶

פתחו את הדפדפן שלכם בכתובת <http://127.0.0.1:8000/items/5?q=somequery>.

אתם תראו תגובת JSON:

    
    
    {"item_id": 5, "q": "somequery"}
    

כבר יצרתם API ש:

  * מקבל בקשות HTTP בנתיבים `/` ו - `/items/{item_id}`.
  * שני ה _נתיבים_ מקבלים _בקשות_ `GET` (ידועות גם כ _מתודות_ HTTP).
  * ה _נתיב_ `/items/{item_id}` כולל *פרמטר נתיב_ `item_id` שאמור להיות `int`.
  * ה _נתיב_ `/items/{item_id}` *פרמטר שאילתא_ אופציונלי `q`.

### תיעוד API אינטרקטיבי¶

כעת פנו לכתובת <http://127.0.0.1:8000/docs>.

אתם תראו את התיעוד האוטומטי (מסופק על ידי [Swagger
UI](https://github.com/swagger-api/swagger-ui)):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-
simple.png)

### תיעוד אלטרנטיבי¶

כעת פנו לכתובת <http://127.0.0.1:8000/redoc>.

אתם תראו תיעוד אלטרנטיבי (מסופק על ידי
[ReDoc](https://github.com/Rebilly/ReDoc)):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## שדרוג לדוגמא¶

כעת ערכו את הקובץ `main.py` כך שיוכל לקבל גוף מבקשת `PUT`.

הגדירו את הגוף בעזרת רמזי טיפוסים סטנדרטיים, הודות ל - `Pydantic`.

    
    
    from typing import Union
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        price: float
        is_offer: Union[bool, None] = None
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    
    
    @app.put("/items/{item_id}")
    def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}
    

השרת אמול להתאתחל אוטומטית (מאחר והוספתם `--reload` לפקודת `uvicorn` שלמעלה).

### שדרוג התיעוד האינטרקטיבי¶

כעת פנו לכתובת <http://127.0.0.1:8000/docs>.

  * התיעוד האוטומטי יתעדכן, כולל הגוף החדש:

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

  * לחצו על הכפתור "Try it out", הוא יאפשר לכם למלא את הפרמטרים ולעבוד ישירות מול ה - API.

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

  * אחר כך לחצו על הכפתור "Execute", האתר יתקשר עם ה - API שלכם, ישלח את הפרמטרים, ישיג את התוצאות ואז יראה אותן על המסך:

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### שדרוג התיעוד האלטרנטיבי¶

כעת פנו לכתובת <http://127.0.0.1:8000/redoc>.

  * התיעוד האלטרנטיבי גם יראה את פרמטר השאילתא והגוף החדשים.

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### סיכום¶

לסיכום, אתם מכריזים ** פעם אחת** על טיפוסי הפרמטרים, גוף וכו' כפרמטרים
לפונקציה.

אתם עושים את זה עם טיפוסי פייתון מודרניים.

אתם לא צריכים ללמוד תחביר חדש, מתודות או מחלקות של ספרייה ספיציפית, וכו'

רק **פייתון 3.6+** סטנדרטי.

לדוגמא, ל - `int`:

    
    
    item_id: int
    

או למודל `Item` מורכב יותר:

    
    
    item: Item
    

...ועם הכרזת הטיפוס האחת הזו אתם מקבלים:

  * תמיכת עורך, כולל:
    * השלמות.
    * בדיקת טיפוסים.
  * אימות מידע:
    * שגיאות ברורות ואטומטיות כאשר מוכנס מידע לא חוקי .
    * אימות אפילו לאובייקטי JSON מקוננים.
  * המרה של מידע קלט: המרה של מידע שמגיע מהרשת למידע וטיפוסים של פייתון. קורא מ:
    * JSON.
    * פרמטרי נתיב.
    * פרמטרי שאילתא.
    * עוגיות.
    * כותרות.
    * טפסים.
    * קבצים.
  * המרה של מידע פלט: המרה של מידע וטיפוסים מפייתון למידע רשת (כ - JSON):
    * המירו טיפוסי פייתון (`str`, `int`, `float`, `bool`, `list`, etc).
    * עצמי `datetime`.
    * עצמי `UUID`.
    * מודלי בסיסי נתונים.
    * ...ורבים אחרים.
  * תיעוד API אוטומטי ואינטרקטיבית כולל שתי אלטרנטיבות לממשק המשתמש:
    * Swagger UI.
    * ReDoc.

* * *

בחזרה לדוגמאת הקוד הקודמת, **FastAPI** ידאג:

  * לאמת שיש `item_id` בנתיב בבקשות `GET` ו - `PUT`.
  * לאמת שה - `item_id` הוא מטיפוס `int` בבקשות `GET` ו - `PUT`.
    * אם הוא לא, הלקוח יראה שגיאה ברורה ושימושית.
  * לבדוק האם קיים פרמטר שאילתא בשם `q` (קרי `http://127.0.0.1:8000/items/foo?q=somequery`) לבקשות `GET`.
    * מאחר והפרמטר `q` מוגדר עם ` = None`, הוא אופציונלי.
    * לולא ה - `None` הוא היה חובה (כמו הגוף במקרה של `PUT`).
  * לבקשות `PUT` לנתיב `/items/{item_id}`, לקרוא את גוף הבקשה כ - JSON:
    * לאמת שהוא כולל את מאפיין החובה `name` שאמור להיות מטיפוס `str`.
    * לאמת שהוא כולל את מאפיין החובה `price` שחייב להיות מטיפוס `float`.
    * לבדוק האם הוא כולל את מאפיין הרשות `is_offer` שאמור להיות מטיפוס `bool`, אם הוא נמצא.
    * כל זה יעבוד גם לאובייקט JSON מקונן.
  * להמיר מ - JSON ול- JSON אוטומטית.
  * לתעד הכל באמצעות OpenAPI, תיעוד שבו יוכלו להשתמש:
    * מערכות תיעוד אינטרקטיביות.
    * מערכות ייצור קוד אוטומטיות, להרבה שפות.
  * לספק ישירות שתי מערכות תיעוד רשתיות.

* * *

רק גרדנו את קצה הקרחון, אבל כבר יש לכם רעיון של איך הכל עובד.

נסו לשנות את השורה:

    
    
        return {"item_name": item.name, "item_id": item_id}
    

...מ:

    
    
            ... "item_name": item.name ...
    

...ל:

    
    
            ... "item_price": item.price ...
    

...וראו איך העורך שלכם משלים את המאפיינים ויודע את הטיפוסים שלהם:

![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

לדוגמא יותר שלמה שכוללת עוד תכונות, ראו את ה[מדריך -
למשתמש](https://fastapi.tiangolo.com/tutorial/).

**התראת ספוילרים** : המדריך - למשתמש כולל:

  * הכרזה על **פרמטרים** ממקורות אחרים ושונים כגון: **כותרות** , **עוגיות** , **טפסים** ו - **קבצים**.
  * איך לקבוע **מגבלות אימות** בעזרת `maximum_length` או `regex`.
  * דרך חזקה וקלה להשתמש ב **הזרקת תלויות**.
  * אבטחה והתאמתות, כולל תמיכה ב - **OAuth2** עם **JWT** והתאמתות **HTTP Basic**.
  * טכניקות מתקדמות (אבל קלות באותה מידה) להכרזת אובייקטי JSON מקוננים (תודות ל - Pydantic).
  * אינטרקציה עם **GraphQL** דרך [Strawberry](https://strawberry.rocks) וספריות אחרות.
  * תכונות נוספות רבות (תודות ל - Starlette) כגון:
    * **WebSockets**
    * בדיקות קלות במיוחד מבוססות על `requests` ו - `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ...ועוד.

## ביצועים¶

בדיקות עצמאיות של TechEmpower הראו שאפליקציות **FastAPI** שרצות תחת Uvicorn הן
[מתשתיות הפייתון המהירות
ביותר](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7),
רק מתחת ל - Starlette ו - Uvicorn עצמן (ש - FastAPI מבוססת עליהן). (*)

כדי להבין עוד על הנושא, ראו את הפרק
[Benchmarks](https://fastapi.tiangolo.com/benchmarks/).

## תלויות אופציונליות¶

בשימוש Pydantic:

  * [`email-validator`](https://github.com/JoshData/python-email-validator) \- לאימות כתובות אימייל.

בשימוש Starlette:

  * [`httpx`](https://www.python-httpx.org) \- דרוש אם ברצונכם להשתמש ב - `TestClient`.
  * [`jinja2`](https://jinja.palletsprojects.com) \- דרוש אם ברצונכם להשתמש בברירת המחדל של תצורת הטמפלייטים.
  * [`python-multipart`](https://github.com/Kludex/python-multipart) \- דרוש אם ברצונכם לתמוך ב "פרסור" טפסים, באצמעות `request.form()`.
  * [`itsdangerous`](https://pythonhosted.org/itsdangerous/) \- דרוש אם ברצונכם להשתמש ב - `SessionMiddleware`.
  * [`pyyaml`](https://pyyaml.org/wiki/PyYAMLDocumentation) \- דרוש אם ברצונכם להשתמש ב - `SchemaGenerator` של Starlette (כנראה שאתם לא צריכים את זה עם FastAPI).

בשימוש FastAPI / Starlette:

  * [`uvicorn`](https://www.uvicorn.org) \- לשרת שטוען ומגיש את האפליקציה שלכם.
  * [`orjson`](https://github.com/ijl/orjson) \- דרוש אם ברצונכם להשתמש ב - `ORJSONResponse`.
  * [`ujson`](https://github.com/esnme/ultrajson) \- דרוש אם ברצונכם להשתמש ב - `UJSONResponse`.

תוכלו להתקין את כל אלו באמצעות `pip install "fastapi[all]"`.

## רשיון¶

הפרויקט הזה הוא תחת התנאים של רשיון MIT.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!

חזרה למעלה

  *[Completion]: also known as auto-complete, autocompletion, IntelliSense
  *[CLI]: ממשק שורת פקודה
  *[Conversion]: also known as: serialization, parsing, marshalling
  *[Dependency Injection]: also known as components, resources, providers, services, injectables
  *["parsing"]: convertir el string que viene de un request HTTP en datos de Python
  *[tip məsləhətlərinə]: Tip Məsləhətləri: Type Hints
  *[otomatik tamamlama]: auto-complete, autocompletion, IntelliSense olaraq da bilinir
  *[_yollarında_]: Yol: Path 
  *[gövdə]: Gövdə: Body 
  *[çevirmək]: Çevrilmə: serialization, parsing, marshalling olaraq da bilinir
  *[Yol]: Yol: Path
  *[Sorğu]: Sorğu: Query
  *[Çərəzlər]: Çərəz: Cookie
  *[Başlıqlaq]: Başlıq: Header
  *[Formalar]: Forma: Form
  *[yolda]: Yol: Path
  *[məcburi olmayan]: Məcburi olmayan: Optional
  *[müştəri]: Müştəri: Client
  *[**başlıqlar**]: Başlıq: Header
  *[çərəzlər]: Çərəz: Cookie
  *[Müqayisələr]: Müqayisələr: Benchmarks
  *[şablon]: Şablon: Template
  *["çevirmə"]: HTTP sorğusu ilə alınan string məlumatın Python obyektinə çevrilməsi
  *[টাইপ্স]: একটি ভেরিয়েবল কি ধরনের ডেটা ধারণ করতে পারে।
  *[রূপান্তর]: যা পরিচিত: serialization, parsing, marshalling
  *[ডিপেন্ডেন্সি ইনজেকশন]: also known as components, resources, providers, services, injectables
  *[Code-Vervollständigung]: auch bekannt als Autovervollständigung, Autocompletion, IntelliSense
  *[ASGI]: Asynchronous Server Gateway Interface – Asynchrone Server-Verbindungsschnittstelle
  *[Body]: Body – Körper, Inhalt: Der eigentliche Inhalt einer Nachricht, nicht die Metadaten
  *[Konvertierung]: auch bekannt als: Serialisierung, Parsen, Marshalling
  *[„parsen“]: Konvertieren des Strings, der aus einer HTTP-Anfrage stammt, nach Python-Daten
  *[Autocompletado]: también conocido como autocompletado, IntelliSense
  *[Conversión]: también conocido como: serialización, parsing, marshalling
  *[Inyección de Dependencias]: también conocido como componentes, recursos, proveedores, servicios, inyectables
  *[واسط خط فرمان]: CLI (Command Line Interface)
  *[سرعت]: Fast
  *[کدنویسی سریع]: Fast to code
  *[باگ کمتر]: Fewer bugs
  *[هوشمندانه]: Intuitive
  *[تکمیل]: یا اتوکامپلیت، اتوکامپلشن، اینتلیسنس
  *[آسان]: Easy
  *[کوچک]: Short
  *[استوار]: Robust
  *[مستندات تعاملی]: Interactive documentation
  *[مبتنی بر استانداردها]: Standards-based
  *[عملیات]: operations در OpenAPI
  *[_پارامتر مسیر_]: Path Parameter
  *[_پارامتر پرسمان_]: Query Parameter
  *[بدنه]: Body
  *[انواع]: Type
  *[نحو]: Syntax
  *[تبدیل]: serialization, parsing, marshalling
  *[پارامترهای مسیر]: Path parameters
  *[پارامترهای پرسمان]: Query parameters
  *[کوکی‌ها]: Cookies
  *[سرآیند‌ها (هدرها)]: Headers
  *[فرم‌ها]: Forms
  *[فایل‌ها]: Files
  *[محدودیت‌های اعتبارسنجی]: Validation Constraints
  *[وب‌سوکت]: WebSocket
  *["تجزیه (parse)"]: تبدیل رشته متنی موجود در درخواست HTTP به انواع داده پایتون
  *[Débogage]: En anglais: Debugging
  *[Complétion]: également connu sous le nom d'auto-complétion, autocomplétion, IntelliSense
  *[ CLI]: Command Line Interface
  *[JSON]: JavaScript Object Notation
  *[paramètre]: en anglais : path parameter
  *[paramètre de requête]: en anglais : query param
  *[le corps]: en anglais : body
  *[Une conversion]: aussi connu sous le nom de : serialization, parsing, marshalling
  *[les paramètres du chemin]: en anglais : path parameters
  *[les paramètres de la requête]: en anglais : query parameters
  *[les en-têtes]: en anglais : headers
  *[les formulaires]: en anglais : forms
  *[les fichiers]: en anglais : files
  *[La conversion]: aussi connu sous le nom de : serialization, parsing, marshalling
  *[en-têtes]: en anglais : headers
  *[système d'injection de dépendance]: aussi connu sous le nom de composants, ressources, fournisseurs, services, injectables
  *[ JWT]: JSON Web Tokens
  *[ JSON]: JavaScript Object Notation
  *[CORS]: Cross-Origin Resource Sharing
  *["décodage"]: convertit la chaine de caractère d'une requête HTTP en donnée Python
  *[השלמה]: ידועה גם כהשלמה אוטומטית או IntelliSense
  *[המרה]: ידועה גם כ: פרסור, סיריאליזציה
  *[הזרקת תלויות]: ידועה גם כרכיבים, משאבים, ספקים, שירותים, מוזרקים
  *["פרסור"]: המרת המחרוזת שמגיעה מבקשת HTTP למידע פייתון



---

# https://fastapi.tiangolo.com/hu/



[ ![logo](img/icon-white.svg) ](. "FastAPI") FastAPI

[ fastapi/fastapi  ](https://github.com/fastapi/fastapi "Főoldalra ugrás")

  * FastAPI  [ FastAPI  ](.) Tartalomjegyzék 
    * Szponzorok 
    * Vélemények 
    * **Typer** , a CLI-ok FastAPI-ja 
    * Követelmények 
    * Telepítés 
    * Példa 
      * Hozd létre 
      * Futtasd le 
      * Ellenőrizd 
      * Interaktív API dokumentáció 
      * Alternatív API dokumentáció 
    * Példa frissítése 
      * Interaktív API dokumentáció frissítése 
      * Alternatív API dokumentáció frissítés 
      * Összefoglalás 
    * Teljesítmény 
    * Opcionális követelmények 
    * Licensz 
  * [ Features  ](features/)
  * [ Learn  ](learn/)

Learn

    * [ Python Types Intro  ](python-types/)
    * [ Concurrency and async / await  ](async/)
    * [ Environment Variables  ](environment-variables/)
    * [ Virtual Environments  ](virtual-environments/)
    * [ Tutorial - User Guide  ](tutorial/)

Tutorial - User Guide

      * [ First Steps  ](tutorial/first-steps/)
      * [ Path Parameters  ](tutorial/path-params/)
      * [ Query Parameters  ](tutorial/query-params/)
      * [ Request Body  ](tutorial/body/)
      * [ Query Parameters and String Validations  ](tutorial/query-params-str-validations/)
      * [ Path Parameters and Numeric Validations  ](tutorial/path-params-numeric-validations/)
      * [ Query Parameter Models  ](tutorial/query-param-models/)
      * [ Body - Multiple Parameters  ](tutorial/body-multiple-params/)
      * [ Body - Fields  ](tutorial/body-fields/)
      * [ Body - Nested Models  ](tutorial/body-nested-models/)
      * [ Declare Request Example Data  ](tutorial/schema-extra-example/)
      * [ Extra Data Types  ](tutorial/extra-data-types/)
      * [ Cookie Parameters  ](tutorial/cookie-params/)
      * [ Header Parameters  ](tutorial/header-params/)
      * [ Cookie Parameter Models  ](tutorial/cookie-param-models/)
      * [ Header Parameter Models  ](tutorial/header-param-models/)
      * [ Response Model - Return Type  ](tutorial/response-model/)
      * [ Extra Models  ](tutorial/extra-models/)
      * [ Response Status Code  ](tutorial/response-status-code/)
      * [ Form Data  ](tutorial/request-forms/)
      * [ Form Models  ](tutorial/request-form-models/)
      * [ Request Files  ](tutorial/request-files/)
      * [ Request Forms and Files  ](tutorial/request-forms-and-files/)
      * [ Handling Errors  ](tutorial/handling-errors/)
      * [ Path Operation Configuration  ](tutorial/path-operation-configuration/)
      * [ JSON Compatible Encoder  ](tutorial/encoder/)
      * [ Body - Updates  ](tutorial/body-updates/)
      * [ Dependencies  ](tutorial/dependencies/)

Dependencies

        * [ Classes as Dependencies  ](tutorial/dependencies/classes-as-dependencies/)
        * [ Sub-dependencies  ](tutorial/dependencies/sub-dependencies/)
        * [ Dependencies in path operation decorators  ](tutorial/dependencies/dependencies-in-path-operation-decorators/)
        * [ Global Dependencies  ](tutorial/dependencies/global-dependencies/)
        * [ Dependencies with yield  ](tutorial/dependencies/dependencies-with-yield/)
      * [ Security  ](tutorial/security/)

Security

        * [ Security - First Steps  ](tutorial/security/first-steps/)
        * [ Get Current User  ](tutorial/security/get-current-user/)
        * [ Simple OAuth2 with Password and Bearer  ](tutorial/security/simple-oauth2/)
        * [ OAuth2 with Password (and hashing), Bearer with JWT tokens  ](tutorial/security/oauth2-jwt/)
      * [ Middleware  ](tutorial/middleware/)
      * [ CORS (Cross-Origin Resource Sharing)  ](tutorial/cors/)
      * [ SQL (Relational) Databases  ](tutorial/sql-databases/)
      * [ Bigger Applications - Multiple Files  ](tutorial/bigger-applications/)
      * [ Background Tasks  ](tutorial/background-tasks/)
      * [ Metadata and Docs URLs  ](tutorial/metadata/)
      * [ Static Files  ](tutorial/static-files/)
      * [ Testing  ](tutorial/testing/)
      * [ Debugging  ](tutorial/debugging/)
    * [ Advanced User Guide  ](advanced/)

Advanced User Guide

      * [ Path Operation Advanced Configuration  ](advanced/path-operation-advanced-configuration/)
      * [ Additional Status Codes  ](advanced/additional-status-codes/)
      * [ Return a Response Directly  ](advanced/response-directly/)
      * [ Custom Response - HTML, Stream, File, others  ](advanced/custom-response/)
      * [ Additional Responses in OpenAPI  ](advanced/additional-responses/)
      * [ Response Cookies  ](advanced/response-cookies/)
      * [ Response Headers  ](advanced/response-headers/)
      * [ Response - Change Status Code  ](advanced/response-change-status-code/)
      * [ Advanced Dependencies  ](advanced/advanced-dependencies/)
      * [ Advanced Security  ](advanced/security/)

Advanced Security

        * [ OAuth2 scopes  ](advanced/security/oauth2-scopes/)
        * [ HTTP Basic Auth  ](advanced/security/http-basic-auth/)
      * [ Using the Request Directly  ](advanced/using-request-directly/)
      * [ Using Dataclasses  ](advanced/dataclasses/)
      * [ Advanced Middleware  ](advanced/middleware/)
      * [ Sub Applications - Mounts  ](advanced/sub-applications/)
      * [ Behind a Proxy  ](advanced/behind-a-proxy/)
      * [ Templates  ](advanced/templates/)
      * [ WebSockets  ](advanced/websockets/)
      * [ Lifespan Events  ](advanced/events/)
      * [ Testing WebSockets  ](advanced/testing-websockets/)
      * [ Testing Events: startup - shutdown  ](advanced/testing-events/)
      * [ Testing Dependencies with Overrides  ](advanced/testing-dependencies/)
      * [ Async Tests  ](advanced/async-tests/)
      * [ Settings and Environment Variables  ](advanced/settings/)
      * [ OpenAPI Callbacks  ](advanced/openapi-callbacks/)
      * [ OpenAPI Webhooks  ](advanced/openapi-webhooks/)
      * [ Including WSGI - Flask, Django, others  ](advanced/wsgi/)
      * [ Generate Clients  ](advanced/generate-clients/)
    * [ FastAPI CLI  ](fastapi-cli/)
    * [ Deployment  ](deployment/)

Deployment

      * [ About FastAPI versions  ](deployment/versions/)
      * [ About HTTPS  ](deployment/https/)
      * [ Run a Server Manually  ](deployment/manually/)
      * [ Deployments Concepts  ](deployment/concepts/)
      * [ Deploy FastAPI on Cloud Providers  ](deployment/cloud/)
      * [ Server Workers - Uvicorn with Workers  ](deployment/server-workers/)
      * [ FastAPI in Containers - Docker  ](deployment/docker/)
    * [ How To - Recipes  ](how-to/)

How To - Recipes

      * [ General - How To - Recipes  ](how-to/general/)
      * [ GraphQL  ](how-to/graphql/)
      * [ Custom Request and APIRoute class  ](how-to/custom-request-and-route/)
      * [ Conditional OpenAPI  ](how-to/conditional-openapi/)
      * [ Extending OpenAPI  ](how-to/extending-openapi/)
      * [ Separate OpenAPI Schemas for Input and Output or Not  ](how-to/separate-openapi-schemas/)
      * [ Custom Docs UI Static Assets (Self-Hosting)  ](how-to/custom-docs-ui-assets/)
      * [ Configure Swagger UI  ](how-to/configure-swagger-ui/)
      * [ Testing a Database  ](how-to/testing-database/)
  * [ Reference  ](reference/)

Reference

    * [ `FastAPI` class  ](reference/fastapi/)
    * [ Request Parameters  ](reference/parameters/)
    * [ Status Codes  ](reference/status/)
    * [ `UploadFile` class  ](reference/uploadfile/)
    * [ Exceptions - `HTTPException` and `WebSocketException` ](reference/exceptions/)
    * [ Dependencies - `Depends()` and `Security()` ](reference/dependencies/)
    * [ `APIRouter` class  ](reference/apirouter/)
    * [ Background Tasks - `BackgroundTasks` ](reference/background/)
    * [ `Request` class  ](reference/request/)
    * [ WebSockets  ](reference/websockets/)
    * [ `HTTPConnection` class  ](reference/httpconnection/)
    * [ `Response` class  ](reference/response/)
    * [ Custom Response Classes - File, HTML, Redirect, Streaming, etc.  ](reference/responses/)
    * [ Middleware  ](reference/middleware/)
    * [ OpenAPI  ](reference/openapi/)

OpenAPI

      * [ OpenAPI `docs` ](reference/openapi/docs/)
      * [ OpenAPI `models` ](reference/openapi/models/)
    * [ Security Tools  ](reference/security/)
    * [ Encoders - `jsonable_encoder` ](reference/encoders/)
    * [ Static Files - `StaticFiles` ](reference/staticfiles/)
    * [ Templating - `Jinja2Templates` ](reference/templating/)
    * [ Test Client - `TestClient` ](reference/testclient/)
  * [ FastAPI People  ](fastapi-people/)
  * [ Resources  ](resources/)

Resources

    * [ Help FastAPI - Get Help  ](help-fastapi/)
    * [ Development - Contributing  ](contributing/)
    * [ Full Stack FastAPI Template  ](project-generation/)
    * [ External Links and Articles  ](external-links/)
    * [ FastAPI and friends newsletter  ](newsletter/)
    * [ Repository Management Tasks  ](management-tasks/)
  * [ About  ](about/)

About

    * [ Alternatives, Inspiration and Comparisons  ](alternatives/)
    * [ History, Design and Future  ](history-design-future/)
    * [ Benchmarks  ](benchmarks/)
    * [ Repository Management  ](management/)
  * [ Release Notes  ](release-notes/)

Tartalomjegyzék

  * Szponzorok 
  * Vélemények 
  * **Typer** , a CLI-ok FastAPI-ja 
  * Követelmények 
  * Telepítés 
  * Példa 
    * Hozd létre 
    * Futtasd le 
    * Ellenőrizd 
    * Interaktív API dokumentáció 
    * Alternatív API dokumentáció 
  * Példa frissítése 
    * Interaktív API dokumentáció frissítése 
    * Alternatív API dokumentáció frissítés 
    * Összefoglalás 
  * Teljesítmény 
  * Opcionális követelmények 
  * Licensz 

# FastAPI

[![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-
teal.png)](https://fastapi.tiangolo.com)

_FastAPI keretrendszer, nagy teljesítmény, könnyen tanulható, gyorsan
kódolható, productionre kész_

[
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master)
](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)
[ ![Coverage](https://coverage-
badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ](https://coverage-
badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi) [ ![Package
version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)
](https://pypi.org/project/fastapi) [ ![Supported Python
versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
](https://pypi.org/project/fastapi)

* * *

**Dokumentáció** : <https://fastapi.tiangolo.com>

**Forrás kód** : <https://github.com/fastapi/fastapi>

* * *

A FastAPI egy modern, gyors (nagy teljesítményű), webes keretrendszer API-ok
építéséhez Python -al, a Python szabványos típusjelöléseire építve.

Kulcs funkciók:

  * **Gyors** : Nagyon nagy teljesítmény, a **NodeJS** -el és a **Go** -val egyenrangú (a Starlettenek és a Pydantic-nek köszönhetően). Az egyik leggyorsabb Python keretrendszer.
  * **Gyorsan kódolható** : A funkciók fejlesztési sebességét 200-300 százalékkal megnöveli. *
  * **Kevesebb hiba** : Körülbelül 40%-al csökkenti az emberi (fejlesztői) hibák számát. *
  * **Intuitív** : Kiváló szerkesztő támogatás. Kiegészítés mindenhol. Kevesebb hibakereséssel töltött idő.
  * **Egyszerű** : Egyszerű tanulásra és használatra tervezve. Kevesebb dokumentáció olvasással töltött idő.
  * **Rövid** : Kód duplikáció minimalizálása. Több funkció minden paraméter deklarálásával. Kevesebb hiba.
  * **Robosztus** : Production ready kód. Automatikus interaktív dokumentáció val.
  * **Szabvány alapú** : Az API-ok nyílt szabványaira alapuló (és azokkal teljesen kompatibilis): [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (korábban Swagger néven ismert) és a [JSON Schema](https://json-schema.org/).

* Egy production alkalmazásokat építő belső fejlesztői csapat tesztjein alapuló becslés. 

## Szponzorok¶

[![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io?ref=fastapi
"BlockBee Cryptocurrency Payment Gateway")
[![](https://fastapi.tiangolo.com/img/sponsors/platform-
sh.png)](https://platform.sh/try-it-now/?utm_source=fastapi-
signup&utm_medium=banner&utm_campaign=FastAPI-signup-June-2023 "Build, run and
scale your apps on a modern, reliable, and secure PaaS.")
[![](https://fastapi.tiangolo.com/img/sponsors/porter.png)](https://www.porter.run
"Deploy FastAPI on AWS with a few clicks")
[![](https://fastapi.tiangolo.com/img/sponsors/bump-
sh.svg)](https://bump.sh/fastapi?utm_source=fastapi&utm_medium=referral&utm_campaign=sponsor
"Automate FastAPI documentation generation with Bump.sh")
[![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-
badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI
files")
[![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge
"Auth, user management and more for your B2B product")
[![](https://fastapi.tiangolo.com/img/sponsors/coherence.png)](https://www.withcoherence.com/?utm_medium=advertising&utm_source=fastapi&utm_campaign=website
"Coherence")
[![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png)](https://www.mongodb.com/developer/languages/python/python-
quickstart-
fastapi/?utm_campaign=fastapi_framework&utm_source=fastapi_sponsorship&utm_medium=web_referral
"Simplify Full Stack Development with FastAPI & MongoDB")
[![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-
gh "Zuplo: Scale, Protect, Document, and Monetize your FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com?utm_source=fastapi
"liblab - Generate SDKs from FastAPI")
[![](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-
fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy
& scale any full-stack web app on Render. Focus on building apps, not infra.")
[![](https://fastapi.tiangolo.com/img/sponsors/haystack-
fastapi.svg)](https://github.com/deepset-ai/haystack/ "Build powerful search
from composable, open source building blocks")
[![](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/
"Pay as you go for market data")
[![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com?utm_source=fastapi+repo&utm_medium=github+sponsorship
"SDKs for your API | Speakeasy")
[![](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/
"Svix - Webhooks as a service")
[![](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral
"Stainless | Generate best-in-class SDKs")

[További szponzorok](https://fastapi.tiangolo.com/fastapi-people/#sponsors)

## Vélemények¶

" _[...] I'm using **FastAPI** a ton these days. [...] I'm actually planning
to use it for all of my team's **ML services at Microsoft**. Some of them are
getting integrated into the core **Windows** product and some **Office**
products._"

Kabir Khan - **Microsoft** [(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

" _We adopted the **FastAPI** library to spawn a **REST** server that can be
queried to obtain **predictions**. [for Ludwig]_"

Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - **Uber**
[(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

" _ **Netflix** is pleased to announce the open-source release of our **crisis
management** orchestration framework: **Dispatch**! [built with **FastAPI**
]_"

Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix**
[(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

" _I’m over the moon excited about **FastAPI**. It’s so fun!_"

Brian Okken - **[Python Bytes](https://pythonbytes.fm/episodes/show/123/time-
to-right-the-py-wrongs?time_in_sec=855) podcast host**
[(ref)](https://twitter.com/brianokken/status/1112220079972728832)

* * *

" _Honestly, what you've built looks super solid and polished. In many ways,
it's what I wanted **Hug** to be - it's really inspiring to see someone build
that._"

Timothy Crosley - **[Hug](https://github.com/hugapi/hug) creator**
[(ref)](https://news.ycombinator.com/item?id=19455465)

* * *

" _If you're looking to learn one **modern framework** for building REST APIs,
check out **FastAPI** [...] It's fast, easy to use and easy to learn [...]_"

" _We've switched over to **FastAPI** for our **APIs** [...] I think you'll
like it [...]_"

Ines Montani - Matthew Honnibal - **[Explosion AI](https://explosion.ai)
founders - [spaCy](https://spacy.io) creators**
[(ref)](https://twitter.com/_inesmontani/status/1144173225322143744) \-
[(ref)](https://twitter.com/honnibal/status/1144031421859655680)

* * *

" _If anyone is looking to build a production Python API, I would highly
recommend **FastAPI**. It is **beautifully designed** , **simple to use** and
**highly scalable** , it has become a **key component** in our API first
development strategy and is driving many automations and services such as our
Virtual TAC Engineer._"

Deon Pillsbury - **Cisco**
[(ref)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-
activity-6963242628536487936-trAp/)

* * *

## **Typer** , a CLI-ok FastAPI-ja¶

[![](https://typer.tiangolo.com/img/logo-margin/logo-margin-
vector.svg)](https://typer.tiangolo.com)

Ha egy olyan CLI alkalmazást fejlesztesz amit a parancssorban kell használni
webes API helyett, tekintsd meg: [**Typer**](https://typer.tiangolo.com/).

**Typer** a FastAPI kistestvére. A **CLI-k FastAPI-ja**. ⌨️ 🚀

## Követelmények¶

A FastAPI óriások vállán áll:

  * [Starlette](https://www.starlette.io/) a webes részekhez.
  * [Pydantic](https://docs.pydantic.dev/) az adat részekhez.

## Telepítés¶

    
    
    $ pip install fastapi
    
    ---> 100%
    

A production-höz egy ASGI szerverre is szükség lesz, mint például az
[Uvicorn](https://www.uvicorn.org) vagy a
[Hypercorn](https://github.com/pgjones/hypercorn).

    
    
    $ pip install "uvicorn[standard]"
    
    ---> 100%
    

## Példa¶

### Hozd létre¶

  * Hozz létre a `main.py` fájlt a következő tartalommal:

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

Vagy használd az `async def`-et...

Ha a kódod `async` / `await`-et, használ `async def`:

    
    
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    async def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    

**Megjegyzés** :

Ha nem tudod, tekintsd meg a _"Sietsz?"_ szekciót [`async` és `await`-ről
dokumentációba](https://fastapi.tiangolo.com/async/#in-a-hurry).

### Futtasd le¶

Indítsd el a szervert a következő paranccsal:

    
    
    $ uvicorn main:app --reload
    
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [28720]
    INFO:     Started server process [28722]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    

A parancsról `uvicorn main:app --reload`...

A `uvicorn main:app` parancs a következőre utal:

  * `main`: fájl `main.py` (a Python "modul").
  * `app`: a `main.py`-ban a `app = FastAPI()` sorral létrehozott objektum.
  * `--reload`: kód változtatás esetén újra indítja a szervert. Csak fejlesztés közben használandó.

### Ellenőrizd¶

Nyisd meg a böngésződ a következő címen:
<http://127.0.0.1:8000/items/5?q=somequery>.

A következő JSON választ fogod látni:

    
    
    {"item_id": 5, "q": "somequery"}
    

Máris létrehoztál egy API-t ami:

  * HTTP kéréseket fogad a `/` és `/items/{item_id}` _útvonalakon_.
  * Mindkét _útvonal_ a `GET` _műveletet_ használja (másik elnevezés: HTTP _metódus_ ).
  * A `/items/{item_id}` _útvonalnak_ van egy _path paramétere_ , az `item_id`, aminek `int` típusúnak kell lennie.
  * A `/items/{item_id}` _útvonalnak_ még van egy opcionális, `str` típusú _query paramétere_ is, a `q`.

### Interaktív API dokumentáció¶

Most nyisd meg a <http://127.0.0.1:8000/docs> címet.

Az automatikus interaktív API dokumentációt fogod látni (amit a [Swagger
UI](https://github.com/swagger-api/swagger-ui)-al hozunk létre):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-
simple.png)

### Alternatív API dokumentáció¶

És most menj el a <http://127.0.0.1:8000/redoc> címre.

Az alternatív automatikus dokumentációt fogod látni. (lásd
[ReDoc](https://github.com/Rebilly/ReDoc)):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## Példa frissítése¶

Módosítsuk a `main.py` fájlt, hogy `PUT` kérések esetén tudjon body-t fogadni.

Deklaráld a body-t standard Python típusokkal, a Pydantic-nak köszönhetően.

    
    
    from typing import Union
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        price: float
        is_offer: Union[bool, None] = None
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    
    
    @app.put("/items/{item_id}")
    def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}
    

A szerver automatikusan újraindul (mert hozzáadtuk a --reload paramétert a
fenti `uvicorn` parancshoz).

### Interaktív API dokumentáció frissítése¶

Most menj el a <http://127.0.0.1:8000/docs> címre.

  * Az interaktív API dokumentáció automatikusan frissült így már benne van az új body.

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

  * Kattints rá a "Try it out" gombra, ennek segítségével kitöltheted a paramétereket és közvetlen használhatod az API-t:

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

  * Ezután kattints az "Execute" gompra, a felhasználói felület kommunikálni fog az API-oddal. Elküldi a paramétereket és a visszakapott választ megmutatja a képernyődön.

![Swagger UI
interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### Alternatív API dokumentáció frissítés¶

Most menj el a <http://127.0.0.1:8000/redoc> címre.

  * Az alternatív dokumentáció szintúgy tükrözni fogja az új kérési paraméter és body-t.

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### Összefoglalás¶

Összegzésül, deklarálod **egyszer** a paraméterek, body, stb típusát funkciós
paraméterekként.

Ezt standard modern Python típusokkal csinálod.

Nem kell új szintaxist, vagy specifikus könyvtár mert metódósait, stb.
megtanulnod.

Csak standard **Python**.

Például egy `int`-nek:

    
    
    item_id: int
    

Egy komplexebb `Item` modellnek:

    
    
    item: Item
    

... És csupán egy deklarációval megkapod a:

  * Szerkesztő támogatást, beleértve:
    * Szövegkiegészítés.
    * Típus ellenőrzés.
  * Adatok validációja:
    * Automatikus és érthető hibák amikor az adatok hibásak.
    * Validáció mélyen ágyazott objektumok esetén is.
  * Bemeneti adatok átváltása : a hálózatról érkező Python adatokká és típusokká. Adatok olvasása következő forrásokból:
    * JSON.
    * Cím paraméterek.
    * Query paraméterek.
    * Cookie-k.
    * Header-ök.
    * Formok.
    * Fájlok.
  * Kimeneti adatok átváltása: Python adatok is típusokról hálózati adatokká:
    * válts át Python típusokat (`str`, `int`, `float`, `bool`, `list`, etc).
    * `datetime` csak objektumokat.
    * `UUID` objektumokat.
    * Adatbázis modelleket.
    * ...És sok mást.
  * Automatikus interaktív dokumentáció, beleértve két alternatív dokumentációt is:
    * Swagger UI.
    * ReDoc.

* * *

Visszatérve az előző kód példához. A **FastAPI** :

  * Validálja hogy van egy `item_id` mező a `GET` és `PUT` kérésekben.
  * Validálja hogy az `item_id` `int` típusú a `GET` és `PUT` kérésekben.
    * Ha nem akkor látni fogunk egy tiszta hibát ezzel kapcsolatban.
  * ellenőrzi hogyha van egy opcionális query paraméter `q` névvel (azaz `http://127.0.0.1:8000/items/foo?q=somequery`) `GET` kérések esetén.
    * Mivel a `q` paraméter `= None`-al van deklarálva, ezért opcionális.
    * `None` nélkül ez a mező kötelező lenne (mint például a body `PUT` kérések esetén).
  * a `/items/{item_id}` címre érkező `PUT` kérések esetén, a JSON-t a következőképpen olvassa be:
    * Ellenőrzi hogy létezik a kötelező `name` nevű attribútum és `string`.
    * Ellenőrzi hogy létezik a kötelező `price` nevű attribútum és `float`.
    * Ellenőrzi hogy létezik a `is_offer` nevű opcionális paraméter, ami ha létezik akkor `bool`
    * Ez ágyazott JSON objektumokkal is működik
  * JSONről való automatikus konvertálás.
  * dokumentáljuk mindent OpenAPI-al amit használható:
    * Interaktív dokumentációs rendszerekkel.
    * Automatikus kliens kód generáló a rendszerekkel, több nyelven.
  * Hozzá tartozik kettő interaktív dokumentációs web felület.

* * *

Eddig csak a felszínt kapargattuk, de a lényeg hogy most már könnyebben
érthető hogyan működik.

Próbáld kicserélni a következő sorban:

    
    
        return {"item_name": item.name, "item_id": item_id}
    

...ezt:

    
    
            ... "item_name": item.name ...
    

...erre:

    
    
            ... "item_price": item.price ...
    

... És figyeld meg hogy a szerkesztő automatikusan tudni fogja a típusokat és
kiegészíti azokat:

![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

Teljesebb példákért és funkciókért tekintsd meg a [Tutorial - User
Guide](https://fastapi.tiangolo.com/tutorial/) -t.

**Spoiler veszély** : a Tutorial - User Guidehoz tartozik:

  * **Paraméterek** deklarációja különböző helyekről: **header-ök** , **cookie-k** , **form mezők** és **fájlok**.
  * Hogyan állíts be **validációs feltételeket** mint a `maximum_length` vagy a `regex`.
  * Nagyon hatékony és erős **Függőség Injekció** rendszerek.
  * Biztonság és autentikáció beleértve, **OAuth2** , **JWT tokens** és **HTTP Basic** támogatást.
  * Több haladó (de ugyanannyira könnyű) technika **mélyen ágyazott JSON modellek deklarációjára** (Pydantic-nek köszönhetően).
  * **GraphQL** integráció [Strawberry](https://strawberry.rocks)-vel és más könyvtárakkal.
  * több extra funkció (Starlette-nek köszönhetően) pl.:
    * **WebSockets**
    * rendkívül könnyű tesztek HTTPX és `pytest` alapokra építve
    * **CORS**
    * **Cookie Sessions**
    * ...és több.

## Teljesítmény¶

A független TechEmpower benchmarkok szerint az Uvicorn alatt futó **FastAPI**
alkalmazások az [egyik leggyorsabb Python keretrendszerek közé
tartoznak](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7),
éppen lemaradva a Starlette és az Uvicorn (melyeket a FastAPI belsőleg
használ) mögött.(*)

Ezeknek a további megértéséhez:
[Benchmarks](https://fastapi.tiangolo.com/benchmarks/).

## Opcionális követelmények¶

Pydantic által használt:

  * [`email-validator`](https://github.com/JoshData/python-email-validator) \- e-mail validációkra.
  * [`pydantic-settings`](https://docs.pydantic.dev/latest/usage/pydantic_settings/) \- Beállítások követésére.
  * [`pydantic-extra-types`](https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/) \- Extra típusok Pydantic-hoz.

Starlette által használt:

  * [`httpx`](https://www.python-httpx.org) \- Követelmény ha a `TestClient`-et akarod használni.
  * [`jinja2`](https://jinja.palletsprojects.com) \- Követelmény ha az alap template konfigurációt akarod használni.
  * [`python-multipart`](https://github.com/Kludex/python-multipart) \- Követelmény ha "parsing"-ot akarsz támogatni, `request.form()`-al.
  * [`itsdangerous`](https://pythonhosted.org/itsdangerous/) \- Követelmény `SessionMiddleware` támogatáshoz.
  * [`pyyaml`](https://pyyaml.org/wiki/PyYAMLDocumentation) \- Követelmény a Starlette `SchemaGenerator`-ának támogatásához (valószínűleg erre nincs szükség FastAPI használása esetén).

FastAPI / Starlette által használt

  * [`uvicorn`](https://www.uvicorn.org) \- Szerverekhez amíg betöltik és szolgáltatják az applikációdat.
  * [`orjson`](https://github.com/ijl/orjson) \- Követelmény ha `ORJSONResponse`-t akarsz használni.
  * [`ujson`](https://github.com/esnme/ultrajson) \- Követelmény ha `UJSONResponse`-t akarsz használni.

Ezeket mind telepítheted a `pip install "fastapi[all]"` paranccsal.

## Licensz¶

Ez a projekt az MIT license, licensz alatt fut

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!

Vissza a tetejére

  *[Completion]: also known as auto-complete, autocompletion, IntelliSense
  *[CLI]: ממשק שורת פקודה
  *[Conversion]: also known as: serialization, parsing, marshalling
  *[Dependency Injection]: also known as components, resources, providers, services, injectables
  *["parsing"]: converting the string that comes from an HTTP request into Python data
  *[tip məsləhətlərinə]: Tip Məsləhətləri: Type Hints
  *[otomatik tamamlama]: auto-complete, autocompletion, IntelliSense olaraq da bilinir
  *[_yollarında_]: Yol: Path 
  *[gövdə]: Gövdə: Body 
  *[çevirmək]: Çevrilmə: serialization, parsing, marshalling olaraq da bilinir
  *[Yol]: Yol: Path
  *[Sorğu]: Sorğu: Query
  *[Çərəzlər]: Çərəz: Cookie
  *[Başlıqlaq]: Başlıq: Header
  *[Formalar]: Forma: Form
  *[yolda]: Yol: Path
  *[məcburi olmayan]: Məcburi olmayan: Optional
  *[müştəri]: Müştəri: Client
  *[**başlıqlar**]: Başlıq: Header
  *[çərəzlər]: Çərəz: Cookie
  *[Müqayisələr]: Müqayisələr: Benchmarks
  *[şablon]: Şablon: Template
  *["çevirmə"]: HTTP sorğusu ilə alınan string məlumatın Python obyektinə çevrilməsi
  *[টাইপ্স]: একটি ভেরিয়েবল কি ধরনের ডেটা ধারণ করতে পারে।
  *[রূপান্তর]: যা পরিচিত: serialization, parsing, marshalling
  *[ডিপেন্ডেন্সি ইনজেকশন]: also known as components, resources, providers, services, injectables
  *[Code-Vervollständigung]: auch bekannt als Autovervollständigung, Autocompletion, IntelliSense
  *[ASGI]: Asynchronous Server Gateway Interface – Asynchrone Server-Verbindungsschnittstelle
  *[Body]: Body – Körper, Inhalt: Der eigentliche Inhalt einer Nachricht, nicht die Metadaten
  *[Konvertierung]: auch bekannt als: Serialisierung, Parsen, Marshalling
  *[„parsen“]: Konvertieren des Strings, der aus einer HTTP-Anfrage stammt, nach Python-Daten
  *[Autocompletado]: también conocido como autocompletado, IntelliSense
  *[Conversión]: también conocido como: serialización, parsing, marshalling
  *[Inyección de Dependencias]: también conocido como componentes, recursos, proveedores, servicios, inyectables
  *[واسط خط فرمان]: CLI (Command Line Interface)
  *[سرعت]: Fast
  *[کدنویسی سریع]: Fast to code
  *[باگ کمتر]: Fewer bugs
  *[هوشمندانه]: Intuitive
  *[تکمیل]: یا اتوکامپلیت، اتوکامپلشن، اینتلیسنس
  *[آسان]: Easy
  *[کوچک]: Short
  *[استوار]: Robust
  *[مستندات تعاملی]: Interactive documentation
  *[مبتنی بر استانداردها]: Standards-based
  *[عملیات]: operations در OpenAPI
  *[_پارامتر مسیر_]: Path Parameter
  *[_پارامتر پرسمان_]: Query Parameter
  *[بدنه]: Body
  *[انواع]: Type
  *[نحو]: Syntax
  *[تبدیل]: serialization, parsing, marshalling
  *[پارامترهای مسیر]: Path parameters
  *[پارامترهای پرسمان]: Query parameters
  *[کوکی‌ها]: Cookies
  *[سرآیند‌ها (هدرها)]: Headers
  *[فرم‌ها]: Forms
  *[فایل‌ها]: Files
  *[محدودیت‌های اعتبارسنجی]: Validation Constraints
  *[وب‌سوکت]: WebSocket
  *["تجزیه (parse)"]: تبدیل رشته متنی موجود در درخواست HTTP به انواع داده پایتون
  *[Débogage]: En anglais: Debugging
  *[Complétion]: également connu sous le nom d'auto-complétion, autocomplétion, IntelliSense
  *[ CLI]: Command Line Interface
  *[JSON]: JavaScript Object Notation
  *[paramètre]: en anglais : path parameter
  *[paramètre de requête]: en anglais : query param
  *[le corps]: en anglais : body
  *[Une conversion]: aussi connu sous le nom de : serialization, parsing, marshalling
  *[les paramètres du chemin]: en anglais : path parameters
  *[les paramètres de la requête]: en anglais : query parameters
  *[les en-têtes]: en anglais : headers
  *[les formulaires]: en anglais : forms
  *[les fichiers]: en anglais : files
  *[La conversion]: aussi connu sous le nom de : serialization, parsing, marshalling
  *[en-têtes]: en anglais : headers
  *[système d'injection de dépendance]: aussi connu sous le nom de composants, ressources, fournisseurs, services, injectables
  *[ JWT]: JSON Web Tokens
  *[ JSON]: JavaScript Object Notation
  *[CORS]: Cross-Origin Resource Sharing
  *["décodage"]: convertit la chaine de caractère d'une requête HTTP en donnée Python
  *[השלמה]: ידועה גם כהשלמה אוטומטית או IntelliSense
  *[המרה]: ידועה גם כ: פרסור, סיריאליזציה
  *[הזרקת תלויות]: ידועה גם כרכיבים, משאבים, ספקים, שירותים, מוזרקים
  *["פרסור"]: המרת המחרוזת שמגיעה מבקשת HTTP למידע פייתון
  *[Kiegészítés]: más néven auto-complete, autocompletion, IntelliSense
  *[ átváltása]: also known as: serialization, parsing, marshalling
  *[átváltása]:  más néven: serialization, parsing, marshalling
  *[Függőség Injekció]: also known as components, resources, providers, services, injectables



---

