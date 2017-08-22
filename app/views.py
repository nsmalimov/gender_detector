import json

from flask import request
from flask import send_file, make_response
from flask.templating import render_template
from werkzeug.utils import secure_filename

from app.util.funcs import *
from run import app

@app.route('/')
def hello_world():
    return render_template("index.html")


# @app.route('/partials/<path:path>')
# def serve_partial(path):
#     return render_template('/partials/{}'.format(path))
#
#
# @app.route('/data_upload/<project_id>', methods=['GET', 'POST'])
# def upload_data(project_id):
#     if request.method == 'POST':
#         file = request.files['file']
#         filename = secure_filename(file.filename)
#
#         save_file(file, filename, project_id, "data")
#
#         data = Data(filename)
#
#         db.session.add(data)
#         db.session.commit()
#
#         project = Project.query.filter_by(id=project_id).first()
#         project.records.append(data)
#
#         db.session.commit()
#
#         return 'file uploaded successfully'
#
#
# @app.route('/algorithm_upload/<project_id>', methods=['GET', 'POST'])
# def upload_algorithm(project_id):
#     if request.method == 'POST':
#         title = request.form.get('title')
#         description = request.form.get('description')
#         file = request.files['file']
#
#         filename = secure_filename(file.filename)
#         save_file(file, filename, project_id, "algorithms")
#
#         algorithm = Algorithm(title, description, False, filename)
#
#         db.session.add(algorithm)
#         db.session.commit()
#
#         project = Project.query.filter_by(id=project_id).first()
#         project.algorithms.append(algorithm)
#
#         db.session.commit()
#
#         return 'algorithm uploaded successfully'
#
#
# @app.route('/image/<string:image_name>')
# def local_photo(image_name):
#     filename = app.config['IMAGES_FOLDER'] + "/" + image_name
#     return send_file(filename, mimetype='image/gif')
#
#
# @app.route('/object/<project_id>/<object_type>/<string:file_name>')
# def get_object(project_id, object_type, file_name):
#     filepath = load_object(project_id, object_type, file_name)
#     return send_file(filepath)
#
#
# @app.route('/project_create', methods=['POST'])
# def create_project():
#     jsonData = request.get_json()
#     title = jsonData["title"]
#     description = jsonData["description"]
#
#     project = Project(title, description)
#
#     db.session.add(project)
#     db.session.commit()
#
#     project = Project.query.filter_by(title=title).first()
#
#     create_project_files(project.id)
#
#     return 'project created successfully'
#
#
# @app.route('/project_load_all', methods=['GET'])
# def load_all_projects():
#     all_projects = Project.query.all()
#     return make_response(json.dumps([i.serialize for i in all_projects]))
#
#
# @app.route('/data_load_all_by_project', methods=['POST'])
# def load_all_data_by_project():
#     jsonData = request.get_json()
#     project_id = jsonData["project_id"]
#
#     all_data_by_project = Data.query.filter(Data.project_id == project_id).all()
#
#     return make_response(json.dumps([i.serialize for i in all_data_by_project]))
#
#
# @app.route('/algorithm_load_all_by_project', methods=['POST'])
# def load_all_algorithms_by_project():
#     jsonData = request.get_json()
#     project_id = jsonData["project_id"]
#
#     all_algorithms_by_project = Algorithm.query.filter(Algorithm.project_id == project_id).all()
#
#     return make_response(json.dumps([i.serialize for i in all_algorithms_by_project]))
#
#
# @app.route('/delete_object', methods=['POST'])
# def delete_object():
#     jsonData = request.get_json()
#     object_type = jsonData["object_type"]
#     project_id = jsonData["project_id"]
#
#     if (object_type == "project"):
#         Project.query.filter(Project.id == jsonData["id"]).delete()
#     elif (object_type == "data"):
#         Data.query.filter(Data.id == jsonData["id"]).delete()
#         delete_file(jsonData["filename"], project_id, "data")
#     elif (object_type == "algorithm"):
#         Algorithm.query.filter(Algorithm.id == jsonData["id"]).delete()
#         delete_file(jsonData["filename"], project_id, "algorithms")
#
#     db.session.commit()
#
#     return 'object deleted'
#
#
# @app.route('/algorithm_load_common', methods=['GET'])
# def load_common():
#     common_algorithms = Algorithm.query.filter(Algorithm.preloaded == True).all()
#
#     return make_response(json.dumps([i.serialize for i in common_algorithms]))
#
#
# @app.route('/analys_classif_all_result_types', methods=['GET'])
# def load_all_result_types():
#     result_types = ResultTypes.query.all()
#
#     return make_response(json.dumps([i.serialize for i in result_types]))
#
#
# @app.route('/analys_classif_start_processing', methods=['POST'])
# def start_processing():
#     jsonData = request.get_json()
#
#     selectedProject = jsonData['selectedProject']
#     selectedRecord = jsonData['selectedRecord']
#     selectedAlgorithm = jsonData['selectedAlgorithm']
#     selectedResultType = jsonData['selectedResultType']
#
#     project = Project.query.filter_by(id=selectedProject).first()
#     algorithm_1 = Algorithm.query.filter_by(id=selectedAlgorithm).first()
#     result_type_1 = ResultTypes.query.filter_by(id=selectedResultType).first()
#     record_1 = Data.query.filter_by(id=selectedRecord).first()
#
#     analys_classif = AnalysClassif(selectedRecord)
#     db.session.add(analys_classif)
#     db.session.commit()
#
#     analys_classif.algorithms.append(algorithm_1)
#     analys_classif.result_types.append(result_type_1)
#
#     db.session.commit()
#
#     project.analys_classif.append(analys_classif)
#
#     db.session.commit()
#
#     return start_processing_func(project, result_type_1, record_1, algorithm_1, analys_classif)
