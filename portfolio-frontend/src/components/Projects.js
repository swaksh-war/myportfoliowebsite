import React, { Component } from 'react';
import ProjectItems from './ProjectItems';

export default class Projects extends Component {
    constructor() {
        super();
        this.state = {
            projects: [],
            loading: false
        };
    }

    async componentDidMount() {
        this.setState({ loading: true });
        const url = "http://localhost:8000/project/";
        let data = await fetch(url);
        let parsedData = await data.json();
        this.setState({
            projects: parsedData.data,
            loading: false
        });
        console.log(parsedData.message);
    }

    render() {
        const { projects, loading } = this.state;

        if (loading) {
            return (
                <button class="btn btn-primary" type="button" disabled>
                    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                        Loading...
                </button>
            );
        }

        return (
            <div className="container">
                {projects.map((element) => (
                    <ProjectItems
                        key={element.id}
                        name={element.name}
                        description={element.description}
                        started_date={element.started_date}
                        ended_date={element.ended_date}
                    />
                ))}
            </div>
        );
    }
}

