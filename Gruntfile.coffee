module.exports = (grunt) ->
    grunt.initConfig
        bowercopy:
            options:
                # Bower components folder will be removed afterwards
                clean: true
            libs:
                options:
                    destPrefix: 'components'
                files:
                    'js/jquery.min.js': 'bower_components/jquery/dist/jquery.min.js'
                    'js/jquery.min.map': 'bower_components/jquery/dist/jquery.min.map'

                    'js/bootstrap.min.js': 'bower_components/bootstrap/dist/js/bootstrap.min.js'
                    'css/bootstrap.min.css': 'bower_components/bootstrap/dist/css/bootstrap.min.css'

                    'js/underscore.min.js': 'bower_components/underscore/underscore-min.js'
                    'js/underscore-min.map': 'bower_components/underscore/underscore-min.map'

        sass:
            dist:
                files:
                    'yebimom/static/css/yebimom.css': 'yebimom/static/css/yebimom.sass'


    grunt.loadNpmTasks 'grunt-bowercopy'
    grunt.loadNpmTasks 'grunt-contrib-sass'

    grunt.registerTask 'default', [
        'bowercopy'
        'sass'
    ]
