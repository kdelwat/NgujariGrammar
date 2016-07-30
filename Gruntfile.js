module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        node_pandoc: {
            options: {
                flags: '--filter ./filter.py'
            },
            target: {
                expand: true,
                cwd: 'src/content/',
                src: ['*.md'],
                dest: 'build/content/',
                ext: '.html'
            }
        },
        sass: {
            options: {
                sourceMap: true
            },
            dist: {
                files: {
                    'build/css/main.css': 'src/css/main.scss'
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-node-pandoc');
    grunt.loadNpmTasks('grunt-sass')

    grunt.registerTask('default', ['node_pandoc', 'sass']);
}


