'use strict';

window.addEventListener('load', function () {

    
    if (document.getElementById("submit")) {
        document.getElementById("submit").addEventListener("click", function (event) {
            const tweet = document.getElementById('input_tweet').value
            const url = "/sentiment/logreg/result"
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'text/html',
                },
                body: JSON.stringify(tweet),
            })
                .then((res) => res.text())
                .then(function (data) {
                
                    document.getElementById('result').innerText = data
                })
                .catch(function (error) {
                    console.log("Poor girl")
                });
        });
    }


    if (document.getElementById("submit_nb")) {
        document.getElementById("submit_nb").addEventListener("click", function (event) {
            const tweet = document.getElementById('input_tweet_nb').value
            const url = "/sentiment/naivebayes/result"
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(tweet),
            })
                .then((res) => res.text())
                .then(function (data) {

                    document.getElementById('result_nb').innerText = data
                })
                .catch(function (error) {
                    console.log("Poor girl")
                });
    });
    }
});