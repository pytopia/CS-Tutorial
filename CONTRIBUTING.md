# How to Contribute to CS-Tutorial

## Working on a new feature or fixing a bug

If you would like to add a new feature or fix an existing bug, we prefer that you open a new issue on the CS-Tutorial repository before creating a pull request.

It’s important to note that when opening an issue, you should first do a quick search of existing issues to make sure your suggestion hasn’t already been added as an issue.

**To open a Github issue, go to the CS-Tutorial repository, select “Issues”, “New Issue” then “Feature Request” or “Bug Report” and fill out the template.**

The CS-Tutorial team will then get in touch with you to discuss if the proposed feature aligns with the roadmap, and we will guide you along the way in shaping the proposed feature so that it could be merged to the CS-Tutorial codebase.

## What is a Pull Request (PR)?

This is how the GitHub team defines a PR:

> “Pull requests let you tell others about changes you’ve pushed to a branch in a repository on GitHub. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add follow-up commits before your changes are merged into the base branch.”

This process is used by both CS-Tutorial team members and CS-Tutorial contributors to make changes and improvements to CS-Tutorial.

## What to know before opening a PR

### Draft PRs

If you're ready to get some quick initial feedback from the CS-Tutorial team, you can create a draft pull request.

### PRs should be a reasonable length

If your PR is greater than 500 lines, please consider splitting it into multiple smaller contributions.


## How to open a PR and contribute code to CS-Tutorial Open Source

### 1. Forking the CS-Tutorial Repository

Head to CS-Tutorial repository and click ‘Fork’. Forking a repository creates you a copy of the project which you can edit and use to propose changes to the original project.

Once you fork it, a copy of the CS-Tutorial repository will appear inside your GitHub repository list.

### 2. Cloning the Forked Repository Locally

To make changes to your copy of the CS-Tutorial repository, clone the repository on your local machine. To do that, run the following command in your terminal:

```
git clone https://github.com/hejazizo/CS-Tutorial.git
```

The link to the repository can be found after clicking Clone or download button as shown in the image below:

Note: this assumes you have git installed on your local machine. If not, check out the [following guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to learn how to install it.

### 3. Update your Forked Repository

Before you make any changes to your cloned repository, make sure you have the latest version of the original https://github.com/hejazizo/CS-Tutorial.git repository. To do that, run the following commands in your terminal:

```
cd CS-Tutorial
git remote add upstream https://github.com/hejazizo/CS-Tutorial.git
git pull upstream main
```

This will update the local copy of the CS-Tutorial repository to the latest version.

### 4. Implement your code contribution

At this point, you are good to make changes to the files in the local directory of your project.

Alternatively, you can create a new branch which will contain the implementation of your contribution. To do that, run:

```
git checkout -b name-of-your-new-branch
```

### 5. Push changes to your forked repository on GitHub

Once you are happy with the changes you made in the local files, push them to the forked repository on GitHub. To do that, run the following commands:

```
git add .
git commit -m ‘fixed a bug’
git push origin name-of-your-new-branch
```

This will create a new branch on your forked CS-Tutorial repository, and now you’re ready to create a Pull Request with your proposed changes!

### 6. Opening the Pull Request on CS-Tutorial

Head to the forked repository and click on a _Compare & pull_ request button.

This will open a window where you can choose the repository and branch you would like to propose your changes to, as well as specific details of your contribution. In the top panel menu choose the following details:

- Base repository: `hejazizo/cs-tutorial`
- Base branch: `main`
- Head repository: `your-github-username/cs-tutorial`
- Head branch: `name-of-your-new-branch`

Once you are happy with everything, click the _Create pull request_ button. This will create a Pull Request with your proposed changes.

### 8. Merging your PR and the final steps of your contribution

Once you open a PR, a member from the CS-Tutorial team will get in touch with you with the feedback on your contribution. In some cases, contributions are accepted right away, but often, you may be asked to make some edits/improvements. Don’t worry if you are asked to change something - it’s a completely normal part of software development.

If you have been requested to make changes to your contribution, head back to the local copy of your repository on your machine, implement the changes and push them to your contribution branch by repeating instructions from step 5. Your pull request will automatically be updated with the changes you pushed. Once you've implemented all of the suggested changes, tag the person who first reviewed your contribution by mentioning them in the comments of your PR to ask them to take another look.
Finally, if your contribution is accepted, the CS-Tutorial team member will merge it to the CS-Tutorial codebase.

### 10. Non-code contributions

Contributing doesn’t start and end with code. You can support the project by planning community events, creating tutorials, helping fellow community members find answers to their questions or translating documentation and news. Every contribution matters!
