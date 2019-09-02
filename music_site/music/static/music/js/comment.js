var app = angular.module('Comments',[]);
app.controller('CommentsController', function($scope, $http){
    // $scope.commentsList = [{commentsText: 'finish this app', done: false}];
    $http.get('/api/albums/').then(function(response){
        $scope.commentsList = [];
        for (var i = 0; i < response.data.length; i++){
            var comment = {};
            comment.commentsText = response.data[i].text
            comment.done = response.data[i].done
            comment.id = response.data[i].id
            $scope.commentsList.push(comment);
        }
    });
    $scope.saveData = function(){
        var data = {text: $scope.commentsText, done: false}
        $http.put('/api/albums/', data)
    }

    $scope.commentsAdd = function(){
        $scope.commentsList.push({commentsText: $scope.commentsInput, done: false});
        $scope.commentsInput = '';
    };
    $scope.remove = function(){
        var oldList = $scope.commentsList;
        $scope.commentsList = [];
        angular.forEach(oldList, function(comment){
            if (comment.done){
                $http.delete('/api/albums/' + comment.id + '/delete/');
            }
            else{
                $scope.commentsList.push(comment);
            }
        })
    }
})
