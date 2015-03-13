module.exports = (grunt) ->

    grunt.loadNpmTasks 'grunt-bowercopy'

    grunt.registerTask 'default', () ->
        grunt.log.writeln 'hello world'
