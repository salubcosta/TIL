As Seeders são criadas para armazenar dados para teste. Por exemplo. Eu tenho as tabelas a migration usuário. Só que não tem nenhum dado.

No caso acima, eu posso criar uma seeder: <code>php artisan make:seeder UserTableSeeder</code>, e dentro dele posso informar uns dados padrões.
Logo, eu posso criar um usuário padrão para ser criado quando implantar algum projeto.

### Executando as Seeders
<code>php artisan db:seed</code>
