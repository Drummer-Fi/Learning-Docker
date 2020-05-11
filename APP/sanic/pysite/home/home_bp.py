from sanic import Blueprint, response

home_bp = Blueprint('home_blueprint')

home_bp.static('/index.html', './static/index.html')

# @home_bp.route('/')
# async def home_html(request):
#     return await response.file('index.html')\


# @home_bp.route('/index.js')
# async def home_js(request):
