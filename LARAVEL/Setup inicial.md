Primeira configuração. Deixando o laravel global
$ composer global require laravel/installer

Criar este arquivo:
$nano .bash_profile

Depois incluir o seguinte conteúdo dentro do arquivo:
export PATH="$HOME/.config/composer/vendor/bin:$PATH"

Para criar um projeto:
composer create-project --prefer-dist laravel/laravel marketplace_l6 "6.*"

Executar servidor
php artisan serve

Aparentemente para testar conexão com banco, podes executar um php artisan migrate:installer

Criar a primeira migração:
php artisan make:migration create_exemplo_table

Desfazer meleca
php artisan migrate:rollback

Para voltar x passos
php artisan migrate:rollback --steps=3   

Para reexecutar as migrações:
php artisan migrate:refresh

Os seeds servem para alimentar as tabelas

Para reexecutar as migrações e também os seeds:
php artisan migrate:refresh --seed

Executar apenas os seeds:
php artisan db:seed
