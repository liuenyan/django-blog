var gulp = require('gulp'),
    uglify = require('gulp-uglify'),
    minifyCSS = require('gulp-minify-css');

gulp.task('default', ['script', 'css']);

gulp.task('script', function(){
  gulp.src('blog/static/blog/js/*.js')
      .pipe(uglify())
      .pipe(gulp.dest('blog/static/blog/dist/js/'));
});

gulp.task('css', function(){
  gulp.src('blog/static/blog/styles/*.css')
      .pipe(minifyCSS())
      .pipe(gulp.dest('blog/static/blog/dist/css/'));
});
