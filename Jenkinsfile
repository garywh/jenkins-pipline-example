node ('hzbxs-yipin-qatest7-bjzhangjiwei') {

  stage ('Checkout') {
    git 'https://github.com/siwufeiwu/ip2region.git'
  }

  stage ('Install') {
    sh './ci/install.sh'
  }

  stage ('Unit Test') {
    sh './ci/test.sh'
  }

  stage ('Deploy') {
    sh './ci/deploy.sh'
  }
  
}
