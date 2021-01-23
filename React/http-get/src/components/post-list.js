import React, {Component} from 'react'
import axios from 'axios'


class PostList extends Component {

  constructor(props){
    super(props)
    this.state = {
      posts : []
    }
  }

  componentDidMount(){
    axios.get('https://jsonplaceholder.typicode.com/posts')
      .then(response => {
        console.log(response)
        this.setstate({posts: response.data})
      })
      .catch(error => {
        console.log(error)
      })
  }





  render(){
    const { posts } = this.state
    return(
      <div>
        List of Posts
        {
          posts.length ?
          posts.map(post => <div key={post.Id}>{post.Title}</div>):
          null
        }
      </div>
    )
  }
}

export default PostList
