from flask import jsonify, make_response

class ResponseHandler:
    @staticmethod
    def success(data=None, message=None, status_code=200):
        response = {
            'status': 'success',
            'message': message,
            'data': data
        }
        return make_response(jsonify(response), status_code)

    @staticmethod
    def error(message, status_code=400):
        response = {
            'status': 'error',
            'message': message
        }
        return make_response(jsonify(response), status_code)