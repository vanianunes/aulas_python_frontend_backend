import pytest

@pytest.mark.django_db
class TestautenticacaoJWT:
     def test_login_sucesso(self, api_client,regular_user):
          payload = {
               "username": "cliente",
               "password":"user123"
          }
          response = api_client.post('/api/token/',payload)
          assert response.status_code== 200
          assert"access"in response.data
          assert"refresh"in response.data

     def test_login_senha_incorreta(self,api_client,regular_user):
          payload = {
               "username":"cliente",
               "password":"senha_errada"
          }
          response = api_client.post('/api/token/',payload)
          assert response.status_code ==401
          assert response.data['detail'] == "No active account found with the given credentials"

     def test_login_usuario_inexistente(self,api_client):
          payload = {
               "username":"fantasma",
               "password":"qualquersenha"

          }
          response = api_client.post('/api/token/',payload)
          assert response.status_code == 401