module.exports = (grunt) ->
    grunt.initConfig
        clean: [
            'components'
            'static'
        ]

        bowercopy:
            options:
                # Bower components folder will be removed afterwards
                clean: true
            libs:
                options:
                    destPrefix: 'components'
                files:
                    'js/jquery.min.js': 'jquery/dist/jquery.min.js'
                    'js/jquery.min.map': 'jquery/dist/jquery.min.map'

                    'js/jquery-ui.min.js': 'jquery-ui/jquery-ui.min.js'
                    'css/jquery-ui-smoothness.min.css': 'jquery-ui/themes/smoothness/jquery-ui.min.css'

                    'js/bootstrap.min.js': 'bootstrap/dist/js/bootstrap.min.js'
                    'css/bootstrap.min.css': 'bootstrap/dist/css/bootstrap.min.css'

                    'js/underscore.min.js': 'underscore/underscore-min.js'
                    'js/underscore-min.map': 'underscore/underscore-min.map'

                    'css/font-awesome.min.css': 'components-font-awesome/css/font-awesome.min.css'
                    'fonts/': 'components-font-awesome/fonts/'

        compass:
            dist:
                options:
                    sassDir: 'yebimom/static/sass'
                    cssDir: 'yebimom/static/css'

        jshint:
            files: ['yebimom/**/*.js']

        shell:
            pep8:
                command: 'pep8'

            unittest:
                command: 'NOSE_NOCAPTURE=1 python manage.py test -v2 --color --noinput'

            # reset_db:
            #     command: [
            #         'rm -rf **/migrations/'
            #         'python manage.py reset_db --noinput'
            #         'python manage.py makemigrations users centers'
            #         'python manage.py migrate'
            #         'python manage.py loaddata regions'
            #     ].join '&&'

            deploy_staticfiles:
                command: 'python manage.py collectstatic --settings="yebimom.settings.production" --ignore "*.sass" --noinput'

        watch:
            compass:
                files: '**/*.scss'
                tasks: 'compass'

            jshint:
                files: '<%= jshint.files %>'
                tasks: 'jshint'

            # models:
            #     files: ['**/models.py', '**/models/*.py']
            #     tasks: 'shell:reset_db'

            django:
                files: '**/*.py'
                tasks: 'test'

        notify:
            pep8:
                options:
                    title: "PEP8 - Success!"
                    message: "A Foolish Consistency is the Hobgoblin of Little Minds"

            unittest:
                options:
                    title: "UnitTest - Suceess!"
                    message: "Keep Calm and Love TDD"


    grunt.loadNpmTasks 'grunt-contrib-clean'
    grunt.loadNpmTasks 'grunt-bowercopy'
    grunt.loadNpmTasks 'grunt-contrib-compass'
    grunt.loadNpmTasks 'grunt-contrib-jshint'
    grunt.loadNpmTasks 'grunt-shell'
    grunt.loadNpmTasks 'grunt-contrib-watch'
    grunt.loadNpmTasks 'grunt-notify'


    grunt.registerTask 'test', [
        'shell:pep8'
        'notify:pep8'
        'shell:unittest'
        'notify:unittest'
    ]

    grunt.registerTask 'dev', [
    ]

    grunt.registerTask 'deploy', [
        'shell:deploy_staticfiles'
    ]

    grunt.registerTask 'default', [
        'clean'
        'bowercopy'
        'compass'
        'jshint'
        'watch'
    ]
