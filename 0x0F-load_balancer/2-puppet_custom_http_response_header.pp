# automate the task of creating a custom HTTP header response,

file { '/etc/nginx/sites-enabled/default':
content => 'server {
  add_header X-Served-By "$HOSTNAME",
}'

}