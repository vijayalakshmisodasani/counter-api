class counter_api {
  exec { 'clone-repo':
    command => '/usr/bin/git clone git@github.com:vijayalakshmisodasani/counter-api.git /home/ubuntu/counter-api',
    creates => '/home/ubuntu/counter-api',
  }

  exec { 'build-counter-image':
    command => '/usr/bin/docker build -t counter-api /home/ubuntu/counter-api',
    require => Exec['clone-repo'],
  }

  exec { 'run-counter-container':
    command => '/usr/bin/docker run -d -p 8082:8082 --name counter-api counter-api',
    unless  => '/usr/bin/docker ps | grep counter-api',
    require => Exec['build-counter-image'],
  }
}

include counter_api
