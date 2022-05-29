properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/VChes/devop07.git"
    }
    stage("show file"){
        sh "ls -l"
    }
}
