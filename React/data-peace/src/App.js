import React, {Component} from 'react';
import './App.css';
import ReactTable from "react-table";
import "react-table/react-table.css"

class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      posts : []
    }
  }



  componentDidMount(){
    const url = "https://demo9197058.mockable.io/users";
    fetch(url,{
      method: "GET"
    }).then(response => response.json()).then(posts => {
      this.setState({posts: posts})
    })
  }


  render(){
    const columns = [
      {
        Header: "ID",
        accessor: "id",
        style:{
          textAlign: "center"
        },
        width: 40,
        sortable: false,
      },
      {
        Header: "First Name",
        accessor: "first_name",
        style:{
          textAlign: "center"
        },
      },
      {
        Header: "Last Name",
        accessor: "last_name",
        style:{
          textAlign: "center"
        },
        filterable: false
      },
      {
        Header: "Company Name",
        accessor: "company_name",
        style:{
          textAlign: "center"
        },
        sortable: false,
        filterable: false
      },
      {
        Header: "City",
        accessor: "city",
        style:{
          textAlign: "center"
        },
        sortable: false,
        filterable: false
      },
      {
        Header: "State",
        accessor: "state",
        style:{
          textAlign: "center"
        },
        sortable: false,
        filterable: false
      },
      {
        Header: "ZIP",
        accessor: "zip",
        style:{
          textAlign: "center"
        },
        sortable: false,
        filterable: false
      },
      {
        Header: "Email",
        accessor: "email",
        style:{
          textAlign: "center"
        },
        sortable: false,
        filterable: false
      },
      {
        Header: "Web",
        accessor: "web",
        style:{
          textAlign: "center"
        },
        sortable: false,
        filterable: false
      },
      {
        Header: "Age",
        accessor: "age",
        style:{
          textAlign: "center"
        },
        sortable: false,
        filterable: false
      },

    ]
    return (
        <ReactTable
          columns = {columns}
          data={this.state.posts}
          filterable
          defaultPageSize={10}
          noDataText = {"Please Wait..."}
          showPaginationTop
        >
        </ReactTable>
    );
  }
}

export default App;
