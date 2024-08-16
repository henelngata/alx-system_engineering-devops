# kill_process.pp

# Kill the process named 'killmenow' using pkill
exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/bin/pgrep killmenow',
}