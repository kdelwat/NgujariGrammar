module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        node_pandoc: {
            options: {
                flags: '--include-in-header ./src/html/header.html --filter ./filter.py'
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
        },
        uglify: {
            options: {},
            dist: {
                files: {
                    'build/js/main.js': 'src/js/main.js'
                }
            }
        },
        jshint: {
            options: {},
            dist: {
                files: {
                    'build/js/main.js': 'src/js/main.js'
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-node-pandoc');
    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-jshint')

    grunt.registerTask('default', ['node_pandoc', 'sass', 'uglify', 'jshint']);
}


