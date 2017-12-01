# nuggets
For noobies

* [x] GET /containers                     	  List all containers
* [x] GET /containers?state=running       	  List running containers (only)
* [x] GET /containers/<id>	                  Inspect a specific container
* [x] GET /containers/<id>/logs	              Dump specific container logs
* [ ] GET /services		            	          List all service
* [ ] GET /nodes		            	            List all nodes in the swarm
* [x] GET /images		            	            List all images
* [x] POST /containers		            	      Create a new container
* [x] POST /images		            	          Create a new image
* [x] PATCH /images/<id>		            	    Change a specific image's attributes
* [x] PATCH /containers/<id>              	  Change a container's state
* [ ] DELETE /containers                  	  Delete all containers (including running)
* [x] DELETE /containers/<id> 	              Delete a specific container
* [ ] DELETE /images                      	  Delete all images
* [ ] DELETE /images/<id>		                  Delete a specific image

# Notes
- Dockerfile names must be lowercased that is why there is a .lower() in def images_create()
