<template>
    <form class="wrap">
        <div class="search">
            <input type="text" class="searchTerm" placeholder="Enter Item name">
            <button type="submit" class="searchButton">
                <i class="fa fa-search"></i>
            </button>
        </div>  
    </form>
</template>

<script>
export default({
    name : "SearchBar"
})
</script>

<style scoped>
.search {
  width: 100%;
  display: flex;
}

.searchTerm {
  width: 100%;
  height: auto;
  border: 3px solid #508086;
  border-right: none;
  padding: 5px;
  border-radius: 5px 0 0 5px;
  outline: none;
  color: #9DBFAF;
}

.searchTerm:focus{
  color: #508086;
}

.searchButton {
  width: 40px;
  height: auto;
  border: 1px solid #508086;
  background: #508086;
  text-align: center;
  color: #fff;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
  font-size: 20px;
}

/*Resize the wrap to see the search bar change!*/
.wrap{
  width: 40%;
 
}
</style>
