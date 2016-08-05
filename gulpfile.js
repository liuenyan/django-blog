var gulp = require('gulp'),
    uglify = require('gulp-uglify'),
    minifyCSS = require('gulp-minify-css'),
    less = require('gulp-less'),
    rename = require('gulp-rename');

gulp.task('default', ['script', 'less']);

gulp.task('script', function(){
  gulp.src('blog/static/blog/js/*.js')
      .pipe(uglify())
      .pipe(rename({suffix:'.min'}))
      .pipe(gulp.dest('blog/static/blog/dist/js/'));
});

gulp.task('css', function(){
  gulp.src('blog/static/blog/css/*.css')
      .pipe(minifyCSS())
      .pipe(rename({suffix:'.min'}))
      .pipe(gulp.dest('blog/static/blog/dist/css/'));
});

gulp.task('less', function(){
  gulp.src('blog/static/blog/css/*.less')
      .pipe(less())
      .pipe(minifyCSS())
      .pipe(rename({suffix:'.min'}))
      .pipe(gulp.dest('blog/static/blog/dist/css/'));
});
