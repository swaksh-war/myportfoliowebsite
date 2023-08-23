import React, { Component } from 'react'

export default class ProjectItems extends Component {
  render() {
    let {name, description, started_date, ended_date} = this.props
    return (
        <div>
            <div className="card">
                <div className="card-body">
                    <h5 className="card-title">{name}</h5>
                    <p className="card-text">{description}</p>
                    <a href="/" className="card-link">{started_date}</a>
                    <a href="/" className="card-link">{ended_date}</a>
                </div>
            </div>
        </div>
    )
  }
}
