import React from "react";
import axios from 'axios';

class Home extends React.Component{

    componentDidMount(){
        axios.get("http://localhost:8000/tweets/home")
            .then(
                function(response){
                    console.log(response);
                }
            )
    }

    render(){
        return (
            <div>
                <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                    <a className="navbar-brand" href="#">Welcome Akhil</a>
                    <button className="navbar-toggler" type="button" data-toggle="collapse" 
                        data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" 
                        aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav mr-auto">
                            <li className="nav-item active">
                                <a className="nav-link" href="#">Home <span className="sr-only">(current)</span></a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="#">My Tweets</a>
                            </li>
                            <li className="nav-item dropdown">
                                <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" 
                                    data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Users
                                </a>
                                <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                                    {/* {% for user in users %} */}
                                    {/* <a className="dropdown-item" href="{% url 'user_tweets' user.username %}">{{ user }}</a> */}
                                    {/* {% endfor %} */}
                                </div>
                            </li>
                        </ul>
                        <a className="btn btn-info" href="#">Log out</a>
                    </div>
                </nav>
                <main>
                    <div className="container-fluid">
                        {/* {% for tweet in all_tweets %} */}
                        <div className="card">
                            <div className="mx-2 my-2 card-body">
                                {/* <h5 className="card-title">{{tweet.username}}</h5> */}
                            <h6>
                                {/* {{ tweet.content }}&nbsp;&nbsp;&nbsp;&nbsp; */}
                                {/* {% for tag in tweet.tags %} */}
                                {/* <span className="hashtag">#{{ tag }}&nbsp;</span> */}
                                {/* {% endfor %} */}
                            </h6>
                                {/* <span>posted: {{tweet.posted_at}}</span> */}
                                {/* <span>edited: {{tweet.last_edited_at}}</span> */}
                            </div>
                        </div>
                    </div>
                </main>
                <div className="container-fluid mt-4">
                    <p><a href="#">Sign Up</a></p>
                    <p><a href="#">Log In </a></p>
                    <p><a href="#">Log In with Google</a></p>
                </div>
            </div>
        );
    }
}

export default Home;