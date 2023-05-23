# Thoth Management System

This is a Django-based VoIP management system. It features a fully-fledged REST API, allowing for seamless integration with existing systems. The API provides complete CRUD (Create, Retrieve, Update, Delete) functionality, and it's designed with comprehensive filtering, search, and ordering capabilities.

#   Tech Stack
-   Python
-   Django & Django REST Framework
-   SQLite3 (You can replace this with your preferred DBMS)
-   Third-party Django libraries: django_filters, django_cpf_cnpj, phonenumber_field, encrypted_model_fields, corsheaders.

## Installation

1.  Ensure you have Python3 installed on your system.
    
2.  Clone the repository:
`git clone https://github.com/EdsonAugusto/API-THOTH`

3.  Install the required Python dependencies:
    `pip install -r requirements.txt`
    
4.  Apply migrations:
    `python manage.py migrate`
    
 5.  Run the server:
    `python manage.py runserver`

## Usage

API endpoints are located at the following paths:

-   Softswitch_VSC: `api/voip/server_vsc`
-   Server_Gateway: `api/voip/server_gateway`
-   Server_PABx: `api/voip/server_pabx`
-   Server_Portability: `api/voip/server_portability`
-   Server_XenServer: `api/voip/server_xserver`

You can perform `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` operations on each endpoint.

## Notes

Remember to replace the `SECRET_KEY` and `FIELD_ENCRYPTION_KEY` in your `settings.py` file with your own secrets before deploying the application in a production environment.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

