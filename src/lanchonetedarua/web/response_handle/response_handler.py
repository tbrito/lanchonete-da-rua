from flask import jsonify, make_response

class ResponseHandler:
    @staticmethod
    def success(data=None, message=None, status_code=200):

        return make_response(jsonify(data or message), status_code)

    @staticmethod
    def error(message, status_code=400):

        return make_response(jsonify(message), status_code)