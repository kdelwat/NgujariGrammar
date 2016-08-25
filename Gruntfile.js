module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        copy: {
            main: {
                files: [
                    {expand: true,
                     cwd: 'src/',
                     src: ["*.html"],
                     dest: "build/"},
                ],
            },
        },
        node_pandoc: {
            options: {},
            content: {
                options: {
                    flags: '--include-in-header ./src/html/header.html --template ./src/templates/chapter.html --filter ./src/scripts/pandoc_filter.py --toc'
                },
                expand: true,
                cwd: 'src/content/',
                src: ['*.md'],
                dest: 'build/content/',
                ext: '.html'
            },
            texts: {
                options: {
                    flags: '--include-in-header ./src/html/header.html'
                },
                expand: true,
                cwd: 'src/texts/',
                src: ['*.md'],
                dest: 'build/texts/',
                ext: '.html'
            },
        },
        sass: {
            options: {
                sourceMap: true,
                includePaths: ['./node_modules/bulma']
            },
            dist: {
                files: {
                    'build/css/main.css': 'src/css/main.scss'
                },
            },
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
        },
        watch: {
            css: {
                files: '**/*.scss',
                tasks: ['sass'],
                options: {},
            },
            md: {
                files: '**/*.md',
                tasks: ['node_pandoc'],
                options: {},
            },
            html: {
                files: 'src/*.html',
                tasks: ['copy'],
                options: {},
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-node-pandoc');
    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-copy');

    grunt.registerTask('default', ['node_pandoc', 'sass', 'uglify', 'jshint', 'copy']);
}


